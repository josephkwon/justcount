from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Court, Ticket
from django.contrib import messages
from django.core.mail import send_mail
from django.utils import timezone as datetime

# Create your views here.

def index(request):
    court_list = Court.objects.all()
    context = {'court_list': court_list}
    return render(request, 'base/index.html', context)

def court(request, court_id):
    court = get_object_or_404(Court, pk=court_id)
    now=datetime.now()
    ticket_list = Ticket.objects.filter(court=court, served_stamp__gt=now).values_list('id', flat=True)
    if 'court_agent_' + str(court_id) in request.session:
        agent_data = Ticket.objects.filter(court=court, served_stamp__gt=now)
        return render(request, 'base/court.html', {'court': court, 'ticket_list': ticket_list, 'agent_data': agent_data, 'logged_in': True})
    else:
        return render(request, 'base/court.html', {'court': court, 'ticket_list': ticket_list})

def history(request, court_id, page_id):
    page_id = int(page_id)
    if 'court_agent_' + str(court_id) in request.session:
        tickets_per_page = 10
        if page_id == None:
            page_id = 0
        start_ticket = page_id
        end_ticket = start_ticket + tickets_per_page;
        court = get_object_or_404(Court, pk=court_id)
        now=datetime.now()
        tickets = Ticket.objects.filter(court=court, served_stamp__lt=now).order_by('id')
        if len(tickets) < start_ticket:
            messages.error(request, "No tickets on that page.")
            return render(request, 'base/history.html', {'court': court, 'next_page': start_ticket, 'prev_page': max(0,start_ticket - tickets_per_page), 'logged_in': True})
        else:
            return render(request, 'base/history.html', {'court': court, 'history_data': tickets[start_ticket:min(end_ticket, len(tickets))], 'next_page': start_ticket + tickets_per_page, 'prev_page': max(0,start_ticket - tickets_per_page), 'logged_in': True})
    else:
        messages.error(request, "You must be logged in to view history.")
        return HttpResponseRedirect(reverse('base:court', args=court_id))

def reserve(request):
    name = request.POST['name']
    email = request.POST['email']
    message = request.POST['message']
    court_id = request.POST['court_id']

    if not name or not email:
        messages.error(request, "Please enter all fields")
        return HttpResponseRedirect(reverse('base:court', args=court_id))
    try:
        t = Ticket()
        t.name = name
        t.message = message
        t.email = email
        t.court = Court.objects.get(id=court_id)

        send_mail("Ticket Reserved!", "Your ticket number is {}".format(len(Ticket.objects.all()) + 1), "justcountbot@gmail.com", [email], fail_silently=False)

        t.save()

        messages.success(request, "Your ticket has been submitted! Your ticket number is {}".format(t.id))
    except:
        messages.error(request, "Invalid data. Check your email address.")
    return HttpResponseRedirect(reverse('base:court', args=court_id))

def process_ticket(request, court_id):
    if 'court_agent_' + str(court_id) in request.session:
        court = get_object_or_404(Court, pk=court_id)
        now=datetime.now()
        tickets = Ticket.objects.filter(court=court, served_stamp__gt=now).order_by('id')
        if tickets:
            next_ticket = tickets[0]
            next_ticket.served_stamp = now
            next_ticket.save()
            messages.success(request, "Ticket #{} has now been served!".format(next_ticket.id))
        else:
            messages.error(request, "No tickets left to serve.")
    else:
        messages.error(request, "You must be logged in to process a ticket.")
    return HttpResponseRedirect(reverse('base:court', args=court_id))


def login_start(request):
    court_list = Court.objects.all()
    context = {'court_list': court_list}
    return render(request, 'base/login.html', context)

def login_process(request):
    court_id = request.POST['court_id']
    key = request.POST['key']
    actual_key = Court.objects.get(id=court_id).key
    if key == actual_key:
        request.session['court_agent_' + str(court_id)] = True
        messages.success(request, "You've been logged in!")
        return HttpResponseRedirect(reverse('base:court', args=court_id))

    messages.error(request, "Login Failure")
    return HttpResponseRedirect(reverse('base:login_start'))

def logout(request, court_id):
    request.session.flush()
    messages.success(request, "You've been logged out!")
    return HttpResponseRedirect(reverse('base:court', args=court_id))
