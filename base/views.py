from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from .models import Court


# Create your views here.

def index(request):
    court_list = Court.objects.all()
    template = loader.get_template('base/index.html')
    context = RequestContext(request, {
        'court_list': court_list,
    })
    return HttpResponse(template.render(context))


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)
