from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Court, Ticket
from django.contrib import messages
from django.core.mail import send_mail
from django.utils import timezone as datetime
from datetime import timedelta

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
        tickets_per_page = 5
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
        return HttpResponseRedirect(reverse('base:court', kwargs={'court_id':court_id}))

def statistics(request, court_id):
    court = get_object_or_404(Court, pk=court_id)
    now=datetime.now()
    tickets = Ticket.objects.filter(court=court, served_stamp__lt=now).order_by('id')
    avg_time = round(sum(((i.served_stamp - i.request_stamp).seconds/60 for i in tickets))/len(tickets), 2)
    total_served = len(tickets);
    total_served_year = len(tickets.filter(served_stamp__gt=(now-timedelta(days=365))))
    total_served_month = len(tickets.filter(served_stamp__gt=(now-timedelta(days=30))))
    total_served_day = len(tickets.filter(served_stamp__gt=(now-timedelta(days=1))))

    logged_in = False
    if 'court_agent_' + str(court_id) in request.session:
        logged_in = True
    return render(request, 'base/statistics.html', {'court': court, 'avg_time': avg_time, 'total_served': total_served, 'total_served_year': total_served_year, 'total_served_month': total_served_month, 'total_served_day': total_served_day, 'logged_in': logged_in})

def reserve(request):
    name = request.POST['name']
    email = request.POST['email']
    message = request.POST['message']
    court_id = request.POST['court_id']

    if not name or not email:
        messages.error(request, "Please enter all fields")
        return HttpResponseRedirect(reverse('base:court', kwargs={'court_id':court_id}))
    try:
        t = Ticket()
        t.name = name
        t.message = message
        t.email = email
        t.court = Court.objects.get(id=court_id)

        now=datetime.now()
        tickets = Ticket.objects.filter(court=t.court, served_stamp__lt=now).order_by('id')
        queued_tickets = len(Ticket.objects.filter(court=t.court, served_stamp__gt=now))
        avg_time = int(sum(((i.served_stamp - i.request_stamp).seconds/60 for i in tickets))/len(tickets) * queued_tickets)

        send_mail("Ticket Reserved!", "Your ticket number is {}.\nYour estimated wait time is {} minutes.".format(len(Ticket.objects.all()) + 1, avg_time), "justcountbot@gmail.com", [email], fail_silently=False)

        t.save()

        messages.success(request, "Your ticket has been submitted! Your ticket number is {}".format(t.id))
    except:
        messages.error(request, "Invalid data. Check your email address.")
    return HttpResponseRedirect(reverse('base:court', kwargs={'court_id':court_id}))

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
    return HttpResponseRedirect(reverse('base:court', kwargs={'court_id':court_id}))


def login_start(request):
    court_list = Court.objects.all()
    context = {'court_list': court_list}
    return render(request, 'base/login.html', context)

def login_process(request):
    try:
        court_id = request.POST['court_id']
    except:
        messages.error(request, "Please select your court.")
        return HttpResponseRedirect(reverse('base:login_start'))

    key = request.POST['key']
    actual_key = Court.objects.get(id=court_id).key
    if key == actual_key:
        request.session['court_agent_' + str(court_id)] = True
        messages.success(request, "You've been logged in!")
        return HttpResponseRedirect(reverse('base:court', kwargs={'court_id':court_id}))

    messages.error(request, "Login Failure")
    return HttpResponseRedirect(reverse('base:login_start'))

def logout(request, court_id):
    request.session.flush()
    messages.success(request, "You've been logged out!")
    return HttpResponseRedirect(reverse('base:court', kwargs={'court_id':court_id}))
