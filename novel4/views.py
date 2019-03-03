from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, InvalidPage
from django.http import HttpResponse,HttpResponseRedirect
from novel4.models import Shops
from novel4.models import ShopUser
from novel4.models import ShopTag

# Create your views here.

def home(request):
    return render(request,'demo/index.html')

def merchants(request):
    return render(request,'demo/merchantindex.html')


def map(request):
    return render(request,'demo/map.html')