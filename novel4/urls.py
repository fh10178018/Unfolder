from django.conf.urls import url
from django.urls import path
from novel4 import views



urlpatterns = [
    url(r'^$', views.locationshop,name='locationshop'),
    path(r'<str:city>/',views.home,name='home'),
    url(r'^shop/(\d+).html$', views.shop,name='shop'),
    url(r'^s/(\w+).html$', views.categories,name='categories'),
    url(r'^cities$', views.citylist,name='city'),
    url(r'^map$',views.map,name='map'),
]