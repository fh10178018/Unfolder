from django.conf.urls import url
from novel import views

urlpatterns = [
    url(r'^$',views.index),
]