from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, InvalidPage
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.

def home(request):
    return render(request,'demo/index.html')


def map(request):
    return render(request,'demo/map.html')