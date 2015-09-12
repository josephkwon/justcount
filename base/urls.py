from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^reserve_ticket$', views.reserve, name='reserve'),
    url(r'^(?P<court_id>[0-9]+)/?$', views.court, name='court'),
    url(r'^.*$', views.index, name="home"),
]
