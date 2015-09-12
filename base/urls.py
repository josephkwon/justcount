from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login$', views.login_start, name='login_start'),
    url(r'^login_process$', views.login_process, name='login_process'),
    url(r'^reserve_ticket$', views.reserve, name='reserve'),
    url(r'^(?P<court_id>[0-9]+)/?$', views.court, name='court'),
    url(r'^.*$', views.index, name="home"),
]
