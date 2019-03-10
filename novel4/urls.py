from django.conf.urls import url
from django.urls import path
from novel4 import views



urlpatterns = [
    url(r'^$', views.locationshop,name='locationshop'),
    path(r'<str:city>/',views.home,name='home'),
    url(r'^shop/(\d+).html$', views.shop,name='shop'),
    url(r'^s/(\w+)$', views.categories,name='search1'),
    url(r'^map$',views.map,name='map'),
    url(r'^shop/search$', views.search, name='search1'),

]