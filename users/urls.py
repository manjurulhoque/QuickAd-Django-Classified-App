from django.urls import path

from .views import *

app_name = "users"

urlpatterns = [
    path('dashboard', DashboardView.as_view(), name="dashboard"),
]
