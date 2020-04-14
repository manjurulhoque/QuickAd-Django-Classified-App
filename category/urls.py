from django.urls import path, include

from .views import *

app_name = "categories"

urlpatterns = [
    path('', CategoryListView.as_view(), name="list"),
]
