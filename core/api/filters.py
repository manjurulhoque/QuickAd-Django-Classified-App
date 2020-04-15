from django_filters import rest_framework as filters

from core.models import Ad


class AdFilter(filters.FilterSet):
    class Meta:
        model = Ad
        fields = ['category']
