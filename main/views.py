from http.client import HTTPResponse
import json
from django.http import JsonResponse
from unicodedata import category
from django.views.generic import View
from django.shortcuts import render,redirect
from django.db import models
from .models import TourSpot,Category
from django.views.decorators.csrf import csrf_exempt
import pandas as pd


# Create your views here.

# 시작화면
def landing(request):
    return render(
        request,
        'main/main.html',
    )

def map(request):
    mytravel = TourSpot.objects.filter(like = True)
    return render(
        request,
        'main/map.html',{
        'mytravel':mytravel
        }
    )
    



# 전체 대표관광지 리스트
@csrf_exempt
def index(request):
    tourspots = TourSpot.objects.all()
    categories = Category.objects.all()

    if request.method == "POST":
        text = request.POST.get('like_text')
        pk = request.POST.get('pk')
        item = TourSpot.objects.get(pk=pk)

        if item.like ==False:
            item.like = True
            item.save()
            context = {
                'like':item.like,
                'like_text' : "싫어요",
            }
        else:
            item.like = False
            item.save()
            context = {
                'like':item.like,
                'like_text' : "좋아요",
            }
        return JsonResponse(context,status=200)



    return render(
        request,
        'main/index.html',
        {
            'tourspots':tourspots,
            'categories':categories,
        }
    )
    

#카테고리별
def categorypage(request, slug):
    tourspots = TourSpot.objects.all()

    if slug == 'no_category':
        category = '미분류'
        category_posts = TourSpot.objects.filter(category = None)

    else:
        category = Category.objects.get(slug = slug)
        category_posts = TourSpot.objects.filter(category = category)
        
    return render(
        request,
        'main/categorypage.html',
        {
            'category_posts': category_posts,
            'categories': Category.objects.all(),
            'no_category_post_count': TourSpot.objects.filter(category = None).count(),
            'category': category, 
            'tourspots':tourspots,
        }
    )



# 대표관광지 상세
def singlepage(request,pk):
    tourspot = TourSpot.objects.get(pk=pk)
    return render(
        request,
        'main/singlepage.html',{
            'tourspot':tourspot,
        }
    )

#좋아요한 여행지
def myTravel(request):

    mytravel = TourSpot.objects.filter(like = True)

    return render(
        request,
        'main/myTravel.html',
        {'mytravel':mytravel}
    )

