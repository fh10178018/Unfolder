from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, InvalidPage
from django.http import HttpResponse,HttpResponseRedirect
from novel4.models import Shops
from novel4.models import Cities
from novel4.models import ShopUser
from novel4.models import ShopTag

# Create your views here.

def home(request,city):
    view=Shops.objects.get(city=city)
    return render(request,'demo/index.html',{'shops',city})

def shop(request,id):
    view=Shops.objects.get(shop_num=id)
    cat=ShopTag.objects.filter(code1=view.shop_num)
    print()
    return render(request,'demo/merchantindex.html',{'shops':view})



def map(request):
    return render(request,'demo/map.html')