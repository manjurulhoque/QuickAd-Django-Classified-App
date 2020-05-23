from rest_framework import serializers
from django.template.defaultfilters import truncatechars
from django.utils.html import strip_tags
from rest_framework.reverse import reverse_lazy

from ..models import *


class CategorySerializer(serializers.ModelSerializer):
    total_ads = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = "__all__"

    def get_total_ads(self, obj):
        return obj.ad_set.count()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = "__all__"
        exclude = ("password", "user_permissions", "groups", "is_staff", "is_active", "is_superuser", "last_login")


class AdSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    description = serializers.SerializerMethodField()
    url = serializers.SerializerMethodField()
    first_image_or_default = serializers.ReadOnlyField()

    class Meta:
        model = Ad
        fields = "__all__"

    def get_description(self, obj):
        return truncatechars(strip_tags(obj.description), 100)

    def get_url(self, obj):
        return reverse_lazy('ads:ad.details', kwargs={'ad_id': obj.id})
