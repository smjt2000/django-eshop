from django.contrib import admin

from .models import *


class ProductAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'title', 'price', 'active']

    class Meta:
        model = Product


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductGallery)
