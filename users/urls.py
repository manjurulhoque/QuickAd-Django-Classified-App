from django.urls import path

from .views import *

app_name = "users"

urlpatterns = [
    path('dashboard', DashboardView.as_view(), name="dashboard"),
    path('privacy-settings', PrivacySettingsView.as_view(), name="privacy.settings"),
]
