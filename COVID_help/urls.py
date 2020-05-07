from django.contrib import admin
from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name="Index"),
    path('about/', views.about, name="AboutUs"),
    path('info/', views.info, name="AboutUs"),
]