# -*- coding: utf-8 -*-

from django.conf.urls import  url

from apps.NEO.views import  ReturnOtherAddressView, CreateAddressView
from apps.XVG import views

urlpatterns = [
    url(r"^get_other_address", ReturnOtherAddressView.as_view(), name='get_other_address'),
    url(r'^createaddress', CreateAddressView.as_view()),
    url(r'^createaddress', views.post),
]