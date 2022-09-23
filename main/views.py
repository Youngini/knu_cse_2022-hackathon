from unicodedata import category
from django.views.generic import ListView
from django.shortcuts import render
from django.db import models
from .models import TourSpot,Category

# Create your views here.

# 시작화면
def landing(request):
    return render(
        request,
        'main/main.html'
    )

# 전체 대표관광지 리스트
def index(request):
    tourspots = TourSpot.objects.all()
    categories = Category.objects.all()
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


