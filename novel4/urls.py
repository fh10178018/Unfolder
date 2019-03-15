from django.conf.urls import url
from django.urls import path
from novel4 import views



urlpatterns = [
    url(r'^$', views.locationshop,name='locationshop'),
    path(r'<str:city>/',views.home,name='home'),
    url(r'^shop/(\d+).html$', views.shop,name='shop'),
    url(r'^s/(\w+)$', views.categories),
    url(r'^map/(\w+)$',views.map,name='map'),
    url(r'^shop/search1/$', views.search1, name='search1'),
    url(r'^shop/search2/$', views.search2, name='search2'),
    url(r'^user/login/$', views.login, name='login'),
    url(r'^user/regist/$', views.regist, name='regist'),
    url(r'^user/logout/$', views.logout, name='logout'),

]
