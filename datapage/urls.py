# coding=utf-8
from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^$', views.index, name='index'),
    url(r'^index/$', views.index),
    # url(r'^chart/$', views.chart),
    url(r'^$', views.selet),
    # url(r'^zhou/$', views.zhou)
]
