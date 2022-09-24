from django.urls import path
from . import views
from .views import *


urlpatterns = [
    path('', views.landing),
    path('tourSpot',views.index),
    path('tourSpot/<int:pk>/',views.singlepage),
    path("tourSpot/category/<slug>/", views.categorypage),
    path('tourSpot/my/',views.myTravel),
    path('tourSpot/map',views.map),
    #path('tourSpot/my',views.editLike,name='editLike'),
]