from django.conf.urls import url
from novel4 import views

urlpatterns = [
    url(r'^$',views.merchantdemo,name='merchantdemo'),
]