from django.urls import path

from .views import *

app_name = "core"

urlpatterns = [
    path('', IndexView.as_view(), name="home"),
    path('listings', ListingListView.as_view(), name="listings"),
]
