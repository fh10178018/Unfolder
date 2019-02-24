from django.conf.urls import url
from novel3 import views

urlpatterns = [
    url(r'^$',views.home,name='home'),
    url(r'^map$',views.map,name='map'),
]