from django.conf.urls import url
from django.urls import path
from novel4 import views



urlpatterns = [
    path(r'<str:city>/',views.home,name='home'),
    url(r'^shop/(\d+).html$', views.shop,name='shop'),
    url(r'^cities$', views.citylist,name='city'),
    url(r'^map$',views.map,name='map'),
]