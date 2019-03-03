from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, InvalidPage
from django.http import HttpResponse,HttpResponseRedirect
from novel4.models import Shops
from novel4.models import ShopUser
from novel4.models import ShopTag

# Create your views here.

def home(request):
    return render(request,'demo/index.html')

def shop(request,id):
    view=Shops.objects.get(shop_num=id)
    print(view.code.username)
    return render(request,'demo/merchantindex.html',{'shops':view})



def map(request):
    return render(request,'demo/map.html')