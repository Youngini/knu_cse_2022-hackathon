from http.client import HTTPResponse
import json
from unicodedata import category
from django.views.generic import View
from django.shortcuts import render,redirect
from django.db import models
from .models import TourSpot,Category

# Create your views here.

# 시작화면
def landing(request):
    return render(
        request,
        'main/main.html'
    )

class ajaxEX(View):
    def get(self,request):
        text = request.GET.get('button_text')
        print()
        print(text)
        return render(
        request,
        'main/main.html'
    )

# 전체 대표관광지 리스트
def index(request):
    tourspots = TourSpot.objects.all()
    categories = Category.objects.all()

    text = request.POST.get('like_text')
    print()
    print(text)
    
    
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
def edit_like(request):
    likes = TourSpot.objects.all()
    if request.method == 'POST':
        if len(request.POST.getlist('like'))==0:
            like = False
        else:
            like = True
        likes.like = like
        likes.save()

        context = {'like':likes.like}
        print(context)

        return HTTPResponse(json.dumps(context),content_type="application/json")

    



