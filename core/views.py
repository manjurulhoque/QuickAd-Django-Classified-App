from bs4 import BeautifulSoup
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.generic import ListView
import requests

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


@require_http_methods(["GET"])
def get_admin_ajax(request):
    url = request.GET.get('url')
    sessionid = request.GET.get('sessionid')
    cookies = {'sessionid': sessionid}
    results = requests.get(url, cookies=cookies)
    soup = BeautifulSoup(results.content, 'lxml')
    table = str(soup.find_all('table')[0])
    return JsonResponse({'table': table}, safe=True)
