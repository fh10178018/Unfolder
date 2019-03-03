"""Unfolder_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from django.conf.urls import url,include
from novel import views



urlpatterns = [
    # url(r'^admin/',views.adminlogin,name='adminlogin'),
    # path('admin/', admin.site.urls),
    url(r'^$',views.index,name='index'),
    url(r'^admin/',include('novel2.urls')),
    url(r'^demo/',include('novel4.urls')),
    url(r'^merchant/',include('novel3.urls')),
    url(r'^dairy/(\d+).html$', views.dairy)

]
