from django import forms

from .models import *


class AdCreateForm(forms.ModelForm):
    class Meta:
        model = Ad
        exclude = ("user", "ad_image")
