from django.contrib import admin

from .models import *
from .views import get_admin_ajax

_admin_site_get_urls = admin.site.get_urls


class CategoryAdmin(admin.ModelAdmin):
    class Media:
        js = (
            'https://code.jquery.com/jquery-3.1.0.min.js',
            'assets/js/myscript.js',  # project static folder
        )

    def get_urls(self):
        from django.conf.urls import url
        urls = super(CategoryAdmin, self).get_urls()
        # Note that custom urls get pushed to the list (not appended)
        # This doesn't work with urls += ...
        urls = [
                   url(r'^my_view/$', get_admin_ajax),
               ] + urls
        return urls


admin.site.register(Category, CategoryAdmin)
admin.site.register(Ad)
admin.site.register(AdImage)
