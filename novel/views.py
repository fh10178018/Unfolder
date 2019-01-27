from django.shortcuts import render
from novel.models import IndexContents
from novel.models import AdminUser
from novel.models import Webviews
import datetime
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.
def index(request,page=0):
    webviews(1)
    content = IndexContents.objects.filter()
    return render(request, 'home/index.html',{'context':content})

def dairy(request,id):
    view= IndexContents.objects.get(num=id).viewnum+1
    IndexContents.objects.filter(num=id).update(viewnum=view)
    contents=  IndexContents.objects.filter()[:4]
    content = IndexContents.objects.get(num=id)
    editor = AdminUser.objects.get(num=content.editor)
    return render(request,"home/dairy.html",{'context':content,'contexts':contents,'editor':editor})

# 用来记录登陆各网页的次数
def webviews(x):
    data=datetime.datetime.now().strftime('%Y-%m-%d')
    if Webviews.objects.get(time=data) is False:
        Webviews.objects.create(time=data)
    if x==1:
        view = Webviews.objects.get(time=data).view + 1
        Webviews.objects.filter(time=data).update(view=view)
    elif x==2:
        adminview = Webviews.objects.get(time=data).adminview+1
        Webviews.objects.filter(time=data).update(adminview=adminview)
    elif x==3:
        merchantview = Webviews.objects.get(time=data).merchantview+1
        Webviews.objects.filter(time=data).update(merchantview=merchantview)
    else:
        demoview =Webviews.objects.get(time=data).demoview+1
        Webviews.objects.filter(time=data).update(demoview=demoview)