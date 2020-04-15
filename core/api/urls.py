from django.urls import path

from .views import *

urlpatterns = [
    path('ads/', AdListAPIView.as_view()),
    path('categories/', CategoryListAPIView.as_view()),
]
