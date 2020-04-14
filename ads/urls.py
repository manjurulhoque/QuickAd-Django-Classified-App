from django.urls import path

from .views import *

app_name = "ads"

urlpatterns = [
    path('<int:ad_id>', AdDetailsView.as_view(), name="ad.details"),
    path('create', AdCreateView.as_view(), name="crate.ad"),
]
