from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, InvalidPage
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.
def merchantlogin(request):
    return render(request, 'merchant_admin/merchantlogin.html')