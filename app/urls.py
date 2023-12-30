from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home),
    path ('wood/read/<str:pk>', views.Wood_view.getId),
]