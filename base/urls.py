from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^.*$', views.index, name="home"),
]
