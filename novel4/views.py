from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, InvalidPage
from django.http import HttpResponse,HttpResponseRedirect
from novel4.models import Shops
from novel4.models import Cities
from novel4.models import ShopUser
from novel4.models import ShopTag
from novel4.models import ShopMessage
from django.db.models import Q

import json

# Create your views here.
def convert_to_dict(obj):
    '''把Object对象转换成Dict对象'''
    dict = {}
    dict.update(obj.__dict__)
    return dict
def home(request,city):
    if city!= 'cities':
        print(city)
        citynum=Cities.objects.get(encity=city).cityid
        print(citynum)
        shopscity=Shops.objects.filter(city=citynum)
        shopsfood=ShopTag.objects.filter(tag_num__lte=28)    # 美食类（__lte小于等于，__gte大于等于）
        shopsfilm=ShopTag.objects.filter(tag_num=29)      # 影院
        shopssport=ShopTag.objects.filter(Q(tag_num__gte=30)|Q(tag_num__lte=48))      # 运动健身(Q（）|Q（）相当于or)
        shops = Shops.objects.filter(city=citynum)
        shopmessage = ShopMessage.objects.filter()
        return render(request,'demo/index.html',{'shops':shops,'shopsfood':shopsfood,'citynum':citynum,'shopmessage':shopmessage,})
    else:
        return render(request,'demo/citylist.html')

def shop(request,id):
    view=Shops.objects.get(shop_num=id)
    cat=ShopTag.objects.filter(code1=view.shop_num)
    print()
    return render(request,'demo/merchantindex.html',{'shops':view})

def citylist():
    return render(request,'demo/citylist.html')

def map(request):
    return render(request,'demo/map.html')