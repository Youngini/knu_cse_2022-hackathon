from django.urls import path
from . import views


urlpatterns = [
    path('', views.landing),
    path('tourSpot',views.index),
    path('tourSpot/<int:pk>/',views.singlepage),
    path("tourSpot/category/<slug>/", views.categorypage),
]