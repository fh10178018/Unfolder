from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, InvalidPage
from django.http import HttpResponse,HttpResponseRedirect
from novel2.models import AdminUser
from novel2.models import IndexContents
from novel2.models import AdminUserContent
from novel2.models import Webviews
from novel2.models import AdminUserContentComments
from django.shortcuts import redirect
from django.core import serializers
import json
import os
import datetime
from django.contrib.auth import authenticate, login
# Create your views here.

def home(request):
    return render(request,'demo/index.html')