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
        'main/main.html'
    )

def map(request):
    return render(
        request,
        'main/map.html'
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

    # 엑셀에서 카테고리 데이터 가져오기
    filename = 'open_api.xlsx'
    category_excel = pd.read_excel(filename,sheet_name='H2_categoryCode',names = ['Category'],usecols=[3])
    category = category_excel.values.tolist()

    for i in range(len(category)):
        a = str(*category[i])
        Category.objects.create(name=a,slug =a)

    # 엑셀에서 카테고리에 맞는 장소 가져오기
    place_excel = pd.read_excel(filename,sheet_name='H3_areaBasedList',usecols=[1])
    place_cate_excel = pd.read_excel(filename,sheet_name='H3_areaBasedList',usecols=[6])
    location_excel = pd.read_excel(filename,sheet_name='H3_areaBasedList',usecols=[2])
    place = place_excel.values.tolist()
    place_cate = place_cate_excel.values.tolist()
    location = location_excel.values.tolist()

    for i in range(len(place)):
        a = str(*place[i])
        b = str(*place_cate[i])
        c = str(*location[i])

        if(b == 'A01'):
            k = '자연'
        elif(b == 'A02'):
            k = '인문(문화/예술/역사)'        
        elif( b== 'A03'):
            k = '레포츠'
        elif(b == 'A04'):
            k = '쇼핑'
        elif(b == 'A05'):
            k = '음식'
        elif(b == 'B02'):
            k = '숙박'
        else:
            k = '추천코스'
    
        TourSpot.objects.create(place = a,location = c,category = k,like = False)

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

