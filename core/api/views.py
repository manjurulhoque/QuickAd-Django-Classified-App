from django.db.models import Count
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from .serializers import *
from .filters import *


class AdListAPIView(ListAPIView):
    serializer_class = AdSerializer
    queryset = serializer_class.Meta.model.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = AdFilter


class CategoryListAPIView(ListAPIView):
    serializer_class = CategorySerializer
    queryset = serializer_class.Meta.model.objects.all()
