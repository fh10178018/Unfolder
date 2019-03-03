from django.conf.urls import url
from novel4 import views



urlpatterns = [
    url(r'^$',views.home,name='home'),
    url(r'^shop/(\d+).html$', views.shop,name='shop'),
    url(r'^map$',views.map,name='map'),
]