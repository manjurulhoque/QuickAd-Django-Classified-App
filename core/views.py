from django.views.generic import ListView

from core.models import *


class IndexView(ListView):
    template_name = "index.html"
    model = Ad
    context_object_name = "ads"

    def get_queryset(self):
        return self.model.objects.select_related("user").select_related("category").order_by("-created_at")[:6]

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['featured_products'] = Ad.objects.filter(featured=True)
        return context


class ListingListView(ListView):
    model = Ad
    template_name = "listings.html"
    context_object_name = "ads"

    def get_queryset(self):
        return self.model.objects.select_related("category").filter(status=1)
