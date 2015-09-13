from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login$', views.login_start, name='login_start'),
    url(r'^login_process$', views.login_process, name='login_process'),
    url(r'^logout/(?P<court_id>[0-9]+)/?$', views.logout, name='logout'),
    url(r'^history/(?P<court_id>[0-9]+)/(?P<page_id>[0-9]+)/?$', views.history, name='history'),
    url(r'^statistics/(?P<court_id>[0-9]+)/?$', views.statistics, name='stats'),

    url(r'^reserve_ticket$', views.reserve, name='reserve'),
    url(r'^process_ticket/(?P<court_id>[0-9]+)/?$', views.process_ticket, name='process_ticket'),

    url(r'^(?P<court_id>[0-9]+)/?$', views.court, name='court'),
    url(r'^.*$', views.index, name="home"),
]
