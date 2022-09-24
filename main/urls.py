from django.urls import path
from . import views
from .views import *


urlpatterns = [
    path('',ajaxEX.as_view()),
    #path('', views.landing),
    path('tourSpot',views.index),
    path('tourSpot/<int:pk>/',views.singlepage),
    path("tourSpot/category/<slug>/", views.categorypage),
    #path('tourSpot/my',views.edit_like),
    path('tourSpot/my',views.edit_like,name='edit_like'),
]