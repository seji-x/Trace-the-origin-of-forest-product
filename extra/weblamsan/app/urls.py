from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('wood/read/<str:pk>', views.about),
    path('traceability/<str:pk>', views.traceability)
]
