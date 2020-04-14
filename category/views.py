from django.shortcuts import render
from django.views.generic import ListView

from core.models import Category


class CategoryListView(ListView):
    model = Category
    template_name = "categories/index.html"
    context_object_name = "categories"
