from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from core.forms import *
from core.models import *
from core.mixins import CustomLoginRequiredMixin


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class AdCreateView(CustomLoginRequiredMixin, CreateView):
    template_name = 'ads/create.html'
    form_class = AdCreateForm
    success_url = reverse_lazy('accounts:login')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AdCreateView, self).form_valid(form)

    def post(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
