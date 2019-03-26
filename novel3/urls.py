from django.conf.urls import url
from novel3 import views

urlpatterns = [
    url(r'^login$', views.merchantlogin, name='merchantlogin'),
]