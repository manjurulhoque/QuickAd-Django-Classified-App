from django import forms
from django.core.exceptions import ValidationError

from core.models import *


class AdCreateForm(forms.ModelForm):
    class Meta:
        model = Ad
        exclude = ("user",)

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request", None)
        super(AdCreateForm, self).__init__(*args, **kwargs)

    def clean(self):
        self._validate_unique = True
        self.validate_ad_images()
        return self.cleaned_data

    def validate_ad_images(self):
        images = self.request.FILES.getlist('image')
        if images:
            for image in images:
                if image.size > 1 * 1024 * 1024:
                    raise ValidationError("Image file too large ( > 1mb )")
        else:
            raise ValidationError("Couldn't read uploaded images")


class AdUpdateForm(forms.ModelForm):
    class Meta:
        model = Ad
        exclude = ("user",)

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request", None)
        super(AdUpdateForm, self).__init__(*args, **kwargs)

    def clean(self):
        self._validate_unique = True
        if len(self.request.FILES.getlist('image')) > 0:
            self.validate_ad_images()
        return self.cleaned_data

    def validate_ad_images(self):
        images = self.request.FILES.getlist('image')
        if images:
            for image in images:
                if image.size > 1 * 1024 * 1024:
                    raise ValidationError("Image file too large ( > 1mb )")
        else:
            raise ValidationError("Couldn't read uploaded images")


class AdImageForm(forms.ModelForm):
    class Meta:
        model = AdImage
        fields = ("image",)
