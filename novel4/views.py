from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, InvalidPage
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.

def merchantdemo(request):
    return render(request,'merchant_admin/merchant.html')