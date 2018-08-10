# -*- coding: utf-8 -*-

from django.conf.urls import  url

from apps.NEO import celery_test
from apps.NEO import views
from apps.NEO.views import  ReturnOtherAddressView, CreateAddressView

urlpatterns = [
    #请求钱包数据
    # url(r"^get_neo_post", NEOcoinStartView.as_view(), name='getneo'),
    # url(r"^get_neo_get", views.get, name='gettext'),
    #获取其他地址
    url(r"^get_other_address", ReturnOtherAddressView.as_view(), name='get_other_address'),
    url(r'^createaddress', CreateAddressView.as_view()),
    #项目测试
    # url(r"^test_url", views.test_url, name="test_url"),
    #celety测试
    url(r"^celery_test", celery_test.celerytest, name="test_url")
]