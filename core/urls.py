from django.urls import path

from .views import *

app_name = "core"

urlpatterns = [
    path('', IndexView.as_view(), name="home"),
    path('ads/create', AdCreateView.as_view(), name="crate.add"),
]
