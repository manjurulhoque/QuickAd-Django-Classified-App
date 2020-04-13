from django.urls import path

from .views import *

app_name = "core"

urlpatterns = [
    path('', IndexView.as_view(), name="home"),
    path('ads/<int:ad_id>', AdDetailsView.as_view(), name="ad.details"),
    path('ads/create', AdCreateView.as_view(), name="crate.ad"),
]
