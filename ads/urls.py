from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import *

app_name = "ads"

router = SimpleRouter()
router.register(
    prefix=r'search',
    basename='ads',
    viewset=AdViewSet
)

urlpatterns = [
    path('<int:ad_id>', AdDetailsView.as_view(), name="ad.details"),
    path('create', AdCreateView.as_view(), name="crate.ad"),
    path('<int:ad_id>/update', AdUpdateView.as_view(), name="update.ad"),
    path('<int:ad_id>/delete', AdDeleteView.as_view(), name="delete.ad"),
]

urlpatterns += router.urls
