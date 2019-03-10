from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, InvalidPage
from django.http import HttpResponse,HttpResponseRedirect
from novel4.models import Shops
from novel4.models import Cities
from novel4.models import ShopUser
from novel4.models import ShopTag
from novel4.models import ShopMessage
from django.db.models import Q
import urllib.request
import json

# Create your views here.
def convert_to_dict(obj):
    '''把Object对象转换成Dict对象'''
    dict = {}
    dict.update(obj.__dict__)
    return dict
def locationshop(request):
    city = '上海'
    shopsfood = ShopTag.objects.filter(tag_num__lte=28)  # 美食类（__lte小于等于，__gte大于等于）
    shopsfilm = ShopTag.objects.filter(tag_num=29)  # 影院
    shopssport = ShopTag.objects.exclude(Q(tag_num__lt=30) | Q(tag_num__gt=48))  # 休闲娱乐(Q（）|Q（）相当于or)
    shopmessage = ShopMessage.objects.filter()
    return render(request, 'demo/index.html', {'shopsfood': shopsfood, 'shopmessage': shopmessage, 'city': city,'shopssport':shopssport})

def home(request,city):
    if city!= 'cities':
        print (request.user)
        shopsfood=ShopTag.objects.filter(tag_num__lte=28)    # 美食类（__lte小于等于，__gte大于等于）
        shopsfilm=ShopTag.objects.filter(tag_num=29)      # 影院
        shopssport=ShopTag.objects.exclude(Q(tag_num__lt=30)|Q(tag_num__gt=48))      # 运动健身(Q（）|Q（）相当于or)
        shopmessage = ShopMessage.objects.filter()
        return render(request,'demo/index.html',{'shopsfood':shopsfood,'shopmessage':shopmessage,'city':city})
    else:
        cities = Cities.objects.filter()
        newcity={}
        xcity={}
        for item in cities:
            newcity[item.city]=newcity.get(item.city,item.en)
            xcity[item.city]=xcity.get(item.city,item.en[:1])
        print (xcity)
        return render(request, 'demo/citylist.html', {'city': cities,'context':newcity,'xcity':xcity})

def shop(request,id):
    view=Shops.objects.get(shop_num=id)
    cat=ShopTag.objects.filter(code1=view.shop_num)
    print()
    return render(request,'demo/merchantindex.html',{'shops':view})

def citylist(request):
    citist=Cities.objects.filter()
    return render(request,'demo/citylist.html',{'city':citist})

def categories(request,sousuo):
    print (sousuo)
    return render(request,'demo/categories.html')

def map(request):
    return render(request,'demo/map.html')