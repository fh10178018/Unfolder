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



#login 界面
def login1(request):
    if request.method == 'GET':
        return render(request,'my_admin/login.html')
    else:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        try:
            request.session.flush()
            user = AdminUser.objects.filter(num=username, password=password)
        except:
            user = AdminUser.objects.filter(username=username, password=password)
        if user:
            try:
                userlist = AdminUser.objects.get(num=username, password=password)
            except:
                userlist = AdminUser.objects.get(username=username, password=password)
            request.session['username'] = userlist.username
            request.session['usernum'] = userlist.num
            request.session['post'] = userlist.post
            request.session['signature'] = userlist.signature
            request.session['pic'] = userlist.pic
            return redirect("/admin/home/")#进入主页
        else:
            request.session['username1'] = username
            request.session['password_is_wrong'] = True #提出错误
            return redirect("/admin/") #重定向到该url

def logout(request):
    request.session.flush()
    return redirect("/admin/")

#验证是否登陆，登陆后才能访问该页面
def home(request):
    if request.session.get('username')is not None:
        webviews(2)
        view=Webviews.objects.filter().order_by('-time')[:9]
        district1 = {'x': 678, 'y': 867, 'z': 887, 'q': 123, 'l': 200}
        district2 = {'a': 678, 'b': 867, 'c': 887, 'd': 123, 'e': 1200, 'f': 345, 'g': 443}
        return render(request, 'my_admin/index.html',{'views':view,'district1':district1,'district2':district2})
    else:
        return redirect("/admin/")

def adminprofile(request):
    userlcontents = AdminUserContent.objects.filter()[:10]
    context = {
        'userlcontents':userlcontents,
    }
    return render(request,'my_admin/adminprofile.html',context=context)

def adminzone(request):
    return render(request,'my_admin/adminzone.html')

def adminuserlist(request):
    adminusercount = AdminUser.objects.filter().count()
    adminuser = AdminUser.objects.filter()
    #django自带的页数切割
    adminuserpage = Paginator(adminuser, 8)
    if request.method == 'GET':
        # 获取url后的page参数，首页不现实，默认为1
        page =request.GET.get('page')
        try:
            books = adminuserpage.page(page)
        except PageNotAnInteger:
            # 如果请求不是第一页，返回第一页
            books = adminuserpage.page(1)
        except InvalidPage:
            return HttpResponse('找不到页面内容')
        except EmptyPage:
            books = adminuserpage.page(adminusercount)
    return render(request,"my_admin/adminuser_list.html",{'adminuser':books})

def userlist(request):
    return render(request,'my_admin/user_list.html')

def merchantlist(request):
    return render(request,'my_admin/merchant_list.html')

def indexedit(request):
    if request.method == 'GET':
        Contents =IndexContents.objects.filter()
        return render(request,'my_admin/indexedit.html',{'context':Contents})  #以js语言传值
    else:
        headline=request.POST.get("headline")
        name=datetime.datetime.now().strftime('%Y%m%d%H%M%S')+'.jpg' #用时间命名上传文件的名称，防止重复
        subline = request.POST.get("subtitle")
        content = request.POST.get("content")
        editornum=request.session.get('usernum')
        obj = request.FILES.get('file')
        if obj:  # 处理附件上传到方法
            file_path = os.path.join('novel','static', 'newimgs',name)  # 图片保存路径,
            f = open(file_path, 'wb')  # 以二进制写的模式打开
            for chunk in obj.chunks():  # obj.chunks()按块返回文件，通过在for循环中进行迭代，可以将大文件按块写入到服务器中
                f.write(chunk)
            f.close()
        try:
            IndexContents(headline=headline,createtime=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),demo=0,editor=editornum,viewnum=0,likenum=0, subtitile=subline, content=content,firstimg="/static/newimgs/" + name).save()
            return HttpResponse('success')
        except:
            return HttpResponse('error')


def adminuserform(request):
    if request.method == 'GET':
        return render(request, 'my_admin/adminuserform.html')
    else:
        post = request.POST.getlist("posts") #获取多选框
        adminsex = request.POST.get("adminsexs")
        signaqwel = request.POST.get("sig")
        username = request.POST.get("username")
        numid = request.POST.get("num")
        weibourl = request.POST.get("weibourl")
        password = request.POST.get("password")
        headurl = request.POST.get("headurl")
        posts=''
        for i in range(len(post)):
            posts=posts+post[i]
        adminuserAdd = AdminUser(username=username,num=numid,gender=adminsex,password=password,weibo=weibourl,signature=signaqwel,post=posts,pic=headurl)
        # 验证账号是否存在,存在为true
        try:
            num_verify = AdminUser.objects.filter(num=numid)
        except:
            num_verify = False
        if num_verify:
            return HttpResponse('repeat')
        else:
            adminuserAdd.save()
            return HttpResponse('success')

def adminuserdel(request):
    num=request.GET.get('id')
    AdminUser.objects.filter(num=num).delete()
    return redirect("/admin/adminuserlist/")

# 主页面内容删除
def indexeditdel(request):
    num=request.GET.get('removeid')
    IndexContents.objects.filter(num=num).delete()
    return redirect("/admin/indexedit/")

# 置顶次序替换
def indexeditrep(request):
    rdnum=request.GET.get('replacedid')
    rnum=request.GET.get('replaceid')
    rdid=request.GET.get('rdid')
    rid=request.GET.get('rid')
    IndexContents.objects.filter(num=rdnum).update(demo=rid)
    IndexContents.objects.filter(num=rnum).update(demo=rdid)
    return redirect("/admin/indexedit/")

# 内容修改
def indexeditcon(request):
    headline=request.POST.get('headname')
    print(headline)
    subtitle=request.POST.get('subtitle1')
    contents=request.POST.get('contents')
    num=request.GET.get('nid')
    IndexContents.objects.filter(num=num).update(headline=headline,subtitile=subtitle,content=contents)
    return redirect("/admin/indexedit/")

def upload(request):
    if request.method == 'GET':
        img_list = models.Img.objects.all()
        return render(request,'upload.html',{'img_list': img_list})
    elif request.method == "POST":
        user = request.POST.get('user')
        fafafa = request.POST.get('fafafa')
        obj = request.FILES.get('fafafa')
        # print(obj.name,obj.size)  #读取文件名称和大小，返回后台
        # print(user,fafafa)
        file_path = os.path.join('static','newimgs',obj.name)  #文件保存路径
        f = open(file_path, 'wb') #以二进制写的模式打开
        for chunk in obj.chunks():   #obj.chunks()按块返回文件，通过在for循环中进行迭代，可以将大文件按块写入到服务器中
            f.write(chunk)
        f.close()
        IndexContents.firstimg.objects.create(path=file_path)
        ret={'status':True,'path':file_path}
        return HttpResponse(json.dumps(ret))



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