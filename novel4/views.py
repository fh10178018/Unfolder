from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, InvalidPage
from django.http import HttpResponse,HttpResponseRedirect
from novel4.models import Shops
from novel4.models import ShopMessage
from novel4.models import ShopGoods
from novel4.models import ShopEnvironmentPicCopy
from novel4.models import ShopEnvironmentPic
from novel4.models import Categories
from novel4.models import Cities
from novel4.models import ShopUser
from novel4.models import ShopTag
from novel4.models import ShopMessage
from novel4.models import Film
from novel4.models import FilmGoods
from django.db.models import Q
from django.shortcuts import redirect
import urllib.request
import json
import requests
import ajax

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
        shopsfood=ShopTag.objects.filter(tag_num__lte=28)    # 美食类（__lte小于等于，__gte大于等于）
        shopsfilm=ShopTag.objects.filter(tag_num=29)      # 影院
        shopssport = ShopTag.objects.exclude(Q(tag_num__lt=30) | Q(tag_num__gt=48))  # 休闲娱乐(Q（）|Q（）相当于or)
        shopmessage = ShopMessage.objects.filter()
        film = Film.objects.filter().order_by('-film_showtime')[:6]
        for l in film:
            print (l)
        return render(request,'demo/index.html',{'shopsfood':shopsfood,'shopmessage':shopmessage,'city':city,'film':film,'shopssport':shopssport})
    else:
        cities = Cities.objects.filter()
        newcity={}
        xcity={}
        for item in cities:
            newcity[item.city]=newcity.get(item.city,item.en)
            xcity[item.city]=xcity.get(item.city,item.en[:1])
        print (xcity)
        return render(request, 'demo/citylist.html', {'city': cities,'context':newcity,'xcity':xcity})

def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "产生异常"


def shop(request,id):
    view=Shops.objects.get(shop_num=id)
    com=ShopMessage.objects.filter(code5=id)
    num=ShopMessage.objects.filter(code5=id).count()
    menu=ShopGoods.objects.filter(code2=id)
    pic11=ShopEnvironmentPic.objects.filter(code3=id)
    pic2=ShopEnvironmentPicCopy.objects.filter(code3=id)
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
    # cat.sort(cmp=None, key=lambda x: x.code1.shop_grade, reverse=False)
    # for element in cat:
    #     print
    #     (element.code1.shop_num, ":", element.code1.shop_name)

    return render(request,'demo/merchantindex.html',{'shop':shop,'map1':lng,'map2':lat,'tag':list1,'cmd':cmd,'mmm':tage})


def categories(request,sousuo):
    print (sousuo)
    return render(request,'demo/categories.html')

def map(request):
    return render(request,'demo/map.html')

def search(request):
    answer = request.POST.get('search11','')
    select = request.POST.get('select-category','')
    print (answer,select)
    return redirect('/service/s/'+answer)

def 
