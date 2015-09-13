from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Court, Ticket
from django.contrib import messages
from django.core.mail import send_mail
from datetime import datetime

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
        return render(request, 'base/court.html', {'court': court, 'ticket_list': ticket_list, 'agent_data': agent_data})
    else:
        return render(request, 'base/court.html', {'court': court, 'ticket_list': ticket_list})

def reserve(request):
    name = request.POST['name']
    email = request.POST['email']
    message = request.POST['message']
    court_id = request.POST['court_id']

    if not name or not email:
        messages.error(request, "Please enter all fields")
        return HttpResponseRedirect(reverse('base:court', args=court_id))

    t = Ticket()
    t.name = name
    t.message = message
    t.email = email
    t.court = Court.objects.get(id=court_id)
    t.save()

    messages.success(request, "Your ticket has been submitted! Your ticket number is {}".format(t.id))
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

def logout(request):
    request.session.flush()
    return HttpResponse("You are logged out.")
