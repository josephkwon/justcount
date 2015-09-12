from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Court, Ticket


# Create your views here.

def index(request):
    court_list = Court.objects.all()
    context = {'court_list': court_list}
    return render(request, 'base/index.html', context)

def court(request, court_id):
    court = get_object_or_404(Court, pk=court_id)
    return render(request, 'base/court.html', {'court': court})

def reserve(request):
    name = request.POST['name']
    message = request.POST['message']
    court_id = request.POST['court_id']
    
    t = Ticket()
    t.name = name
    t.message = message
    t.court = Court.objects.get(id=court_id)
    t.save()

    return HttpResponseRedirect(reverse('base:court', args=(court_id,)))
