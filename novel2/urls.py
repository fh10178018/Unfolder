from django.conf.urls import url
from novel2 import views

urlpatterns = [
    url(r'^$',views.login1,name='login'),
    url(r'^home/',views.home,name='home'),
    url(r'^adminprofile/',views.adminprofile,name='adminprofile'),
    url(r'^adminzone/',views.adminzone,name='adminzone'),
    url(r'^adminuserlist/', views.adminuserlist, name='adminuserlist'),
    url(r'^userlist/', views.userlist, name='userlist'),
    url(r'^merchantlist/', views.merchantlist, name='merchantlist'),
    url(r'^indexedit/', views.indexedit, name='indexedit'),
    url(r'^indexeditdel/', views.indexeditdel,name='indexeditdel'),
    url(r'^indexeditrep/', views.indexeditrep,name='indexeditrep'),
    url(r'^indexeditcon/', views.indexeditcon,name='indexeditcon'),
    url(r'^adminuserform/', views.adminuserform, name='adminuserform'),
    url(r'^adminuserdel/', views.adminuserdel,name='adminuserdel'),
    url(r'^shopdel/', views.shopdel,name='shopdel'),
    url(r'^logout/', views.logout,name='logout')
    # url(r'^home/',views.admin_home),
]