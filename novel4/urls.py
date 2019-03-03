from django.conf.urls import url
from novel4 import views



urlpatterns = [
    url(r'^$',views.home,name='home'),
    url(r'^merchant$',views.merchants,name='merchant'),
    url(r'^map$',views.map,name='map'),
]