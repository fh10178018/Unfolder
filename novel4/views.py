from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, InvalidPage
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate, login,logout
from novel4.models import Shops
from novel4.models import ShopMessage
from novel4.models import ShopGoods
from novel4.models import ShopEnvironmentPic
from novel4.models import ShopOfficialCopy
from novel4.models import Categories
from novel4.models import Cities
from novel4.models import ShopUser
from novel4.models import ShopTag
from novel4.models import ShopMessage
from novel4.models import Film
from novel4.models import User
from novel4.models import FilmGoods
from django.db.models import Max,Avg,F,Q,Min,Count,Sum
from django.shortcuts import redirect
import jieba
from django_pandas.io import read_frame
import pandas as pd
import numpy as np
import jieba.posseg as psg
import urllib.request
import string
import json
import requests
from math import radians, cos, sin, asin, sqrt


def haversine(lon1, lat1, lon2, lat2):  # 经度1，纬度1，经度2，纬度2 （十进制度数）
    """
    根据经纬度计算距离
    """
    # 将十进制度数转化为弧度
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine公式
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    r = 6371  # 地球平均半径，单位为公里
    return c * r * 1000


# Create your views here.
def convert_to_dict(obj):
    '''把Object对象转换成Dict对象'''
    dict = {}
    dict.update(obj.__dict__)
    return dict

def locationshop(request):
    if request.method == 'GET':
        if request.session.get('username') is None:
            request.session['city'] = '上海'
            city = '上海'
        else:
            city=request.session['city']
        shopsfood = ShopTag.objects.filter(tag_num__lte=28)  # 美食类（__lte小于等于，__gte大于等于）
        shopsfilm = ShopTag.objects.filter(tag_num=29)  # 影院
        shopssport = ShopTag.objects.exclude(Q(tag_num__lt=30) | Q(tag_num__gt=48))  # 休闲娱乐(Q（）|Q（）相当于or)
        shopmessage = ShopMessage.objects.filter()
        film = Film.objects.filter().order_by('-film_showtime')[:6]
        return render(request, 'demo/index.html',
                      {'shopsfood': shopsfood, 'shopmessage': shopmessage, 'city': city, 'film': film,
                       'shopssport': shopssport})
    else:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        try:
            userlist = User.objects.get(username=username, password=password)
            t = 0
        except:
            t = 1
        print (userlist)
        if t == 1:
            return HttpResponse('error')
        else:
            return HttpResponse('success')


def home(request,city):
    if request.method == 'GET':
        if city!= 'cities':
            request.session['city'] = city
            shopsfood=ShopTag.objects.filter(tag_num__lte=28)    # 美食类（__lte小于等于，__gte大于等于）
            shopsfilm=ShopTag.objects.filter(tag_num=29)      # 影院
            shopssport = ShopTag.objects.exclude(Q(tag_num__lt=30) | Q(tag_num__gt=48))  # 休闲娱乐(Q（）|Q（）相当于or)
            shopmessage = ShopMessage.objects.filter()
            film = Film.objects.filter().order_by('-film_showtime')[:6]
            return render(request,'demo/index.html',{'shopsfood':shopsfood,'shopmessage':shopmessage,'city':city,'film':film,'shopssport':shopssport})
        else:
            if request.session.get('username') is None:
                request.session['city'] = '上海'
            cities = Cities.objects.filter()
            newcity={}
            xcity={}
            for item in cities:
                newcity[item.city]=newcity.get(item.city,item.en)
                xcity[item.city]=xcity.get(item.city,item.en[:1])
            return render(request, 'demo/citylist.html', {'city': cities,'context':newcity,'xcity':xcity})
    else:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        print (username,password)

def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "产生异常"


def shop(request,id):
    if request.session.get('username') is None:
        request.session['city'] = '上海'
    view=Shops.objects.get(shop_num=id)
    com=ShopMessage.objects.filter(code5=id)
    num=ShopMessage.objects.filter(code5=id).count()
    menu=ShopGoods.objects.filter(code2=id)
    pic11=ShopEnvironmentPic.objects.filter(code3=id)
    pic2=ShopOfficialCopy.objects.filter(code3=id)
    shop={'shops':view,'mes':com,'cnt':num,'menu':menu,'pic11':pic11,'pic2':pic2}
    url1 = "http://api.map.baidu.com/geocoder/v2/?address="
    url2 = "&output=json&ak=ZLR0ypp2MklnlZ0WHZedVQw4KUpjDwoi"
    place = view.shop_detail_address
    url = url1+place+url2
    a = getHTMLText(url)
    lng = json.loads(a)['result']['location']['lng']
    lat = json.loads(a)['result']['location']['lat']
    list1={}
    for item in com:
        list1[item.tag_libary] = list1.get(item.tag_libary, 0) + 1
    cats=ShopTag.objects.filter(code1=id)
    for line in cats:
        tageid=line.tag_num.cat_id
        tage=line.tag_num
        break
    cmd = ShopTag.objects.filter(tag_num=tageid)
    return render(request,'demo/merchantindex.html',{'shop':shop,'map1':lng,'map2':lat,'tag':list1,'cmd':cmd,'mmm':tage})


def categories(request,sousuo):
    cat = request.GET['cat']
    error_msg = ''
    if not sousuo:
        error_msg = '请输入关键词'
        return render(request,'demo/categories.html',{'error':error_msg})
    if cat == "all-categories":
        instruction1 = Shops.objects.filter( Q(shop_name__icontains=sousuo)|Q(shop_detail_address__contains=sousuo) )
    elif cat == "category1":
        instruction1 = Shops.objects.filter(shop_detail_address__contains=sousuo)
    elif cat == "category2":
        instruction1 = Shops.objects.filter(shop_name__icontains=sousuo)
    sddd=[]
    for line in instruction1:
        s=[]
        s.append(line.shop_lng)
        s.append(line.shop_lat)
        sddd.append(s)
        print (sddd)

    return render(request,'demo/categories.html',{'sgst':instruction1,'sddd':sddd})

def maps(request,sousuo):
    lng = float(request.GET.get('lng'))
    lat = float(request.GET.get('lat'))
    AI(sousuo,lng,lat)
    shop=Shops.objects.filter()
    list=[]
    for line in shop:
        if line.shop_lng and line.shop_lat:
            if lng+0.01>=line.shop_lng and lng-0.01<=line.shop_lng:
                if lat+0.01>=line.shop_lat and lat-0.01<=line.shop_lat:
                    list.append(line)

    return render(request,'demo/map.html',{'shop':list[0:4],'lng':lng,'lat':lat})

def search1(request):
    answer = request.POST.get('search11','')
    select = request.POST.get('select-category','')
    print (answer,select)
    return redirect('/service/s/' + answer + '?cat=' + select)

def search2(request):
    postion = request.POST.get('postion','')
    answer = request.POST.get('mapselect','')
    lng = postion.split(',')[0]
    lat = postion.split(',')[1]
    return redirect('/service/map/'+answer+'?lng='+lng+'&lat='+lat)

def logout(request):
    return redirect('/service/')

def regist(request):
    return redirect('/service/')

def login(request):
    num=request.POST.get('number','')
    password=request.POST.get('password','')

    return redirect('/service/')


def AI(word,lng,lat):
    # 地点未分
    shops=Shops.objects.all()
    shops1 = pd.DataFrame(read_frame(shops))
    shops1['distance']=shops1.apply(lambda row:haversine(lng,lat,row['shop_lng'],row['shop_lat'])<3000,1,0)
    shops2=shops1[shops1['distance']==1]
    print (type(shops2.loc[shops2['shop_name'] == word]))
    print ({(x.word) for x in psg.cut(word)})
    for x in psg.cut(word):
        if x.flag=='nt':
            if shops2[shops2['shop_name']==word].shape[0] == 1:
                print('as这句话是个目的地，我们提供一个单一路径')
                print (shops2[shops2['shop_name']==word].ix[0:1,0])
                return pd.Series(shops2[shops2['shop_name']==word]['shop_num'])
            elif len(shops2[shops2['shop_name'].str.contains(x.word)])==1:
                ('fd这句话是个目的地，我们提供一个单一路径')
            elif len(shops2[shops2['shop_name'].str.contains(x.word)])!=0:
                for x in psg.cut(word):
                    if len(shops2[shops2['shop_name'].str.contains(x.word)])==1:
                        print('fd这句话是个目的地，我们提供一个单一路径')
                        return pd.Series(shops2[shops2['shop_name'].str.contains(x.word)]['shop_num'])
                    elif len(shops2[shops2['shop_name'].str.contains(x.word)])>1:print ('他是个范围')
                    else:break
            else:
                print('没有录入该商铺')
        else:
            print ('不是地点')

