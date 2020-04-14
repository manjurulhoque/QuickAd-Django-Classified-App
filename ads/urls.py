from django.urls import path

from .views import *

app_name = "ads"

urlpatterns = [
    path('<int:ad_id>', AdDetailsView.as_view(), name="ad.details"),
    path('create', AdCreateView.as_view(), name="crate.ad"),
    path('<int:ad_id>/update', AdUpdateView.as_view(), name="update.ad"),
    path('<int:ad_id>/delete', AdDeleteView.as_view(), name="delete.ad"),
]
