import copy

from django.views.generic import TemplateView

from core.mixins import CustomLoginRequiredMixin
from core.models import Ad


class DashboardView(CustomLoginRequiredMixin, TemplateView):
    template_name = "users/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        ads = Ad.objects.filter(user=self.request.user)
        context['ads'] = ads
        total_ads = copy.deepcopy(ads).count()
        featured_ads = copy.deepcopy(ads).filter(featured=True).count()
        context['total_ads'] = total_ads
        context['featured_ads'] = featured_ads
        return context
