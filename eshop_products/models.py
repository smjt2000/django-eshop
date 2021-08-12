from django.db.models import Q
from django.db import models
import os

# Create your models here.
from eshop_products_category.models import ProductCategory


def setFileName(instance, file):
    base_name = os.path.basename(file)
    name, ext = os.path.splitext(base_name)
    final_name = f"{instance.id}-{instance.title}{ext}"
    return f"products/images/{final_name}"


def setGalleryFileName(instance, file):
    base_name = os.path.basename(file)
    name, ext = os.path.splitext(base_name)
    final_name = f"{instance.id}-{instance.title}{ext}"
    return f"products/galleries/{final_name}"


class productManager(models.Manager):
    def search(self, query):
        lookup = Q(title__icontains=query) | Q(description__icontains=query) | Q(tag__title__icontains=query)
        return self.get_queryset().filter(lookup, active=True).distinct()

    def product_by_category(self, category):
        return self.get_queryset().filter(categories__name__iexact=category, active=True)


class Product(models.Model):
    title = models.CharField(max_length=35, verbose_name="عنوان")
    description = models.TextField(verbose_name="توضیحات")
    price = models.IntegerField(verbose_name="قیمت")
    image = models.ImageField(upload_to=setFileName, null=True, blank=True, verbose_name="تصویر")
    active = models.BooleanField(default=True, verbose_name="فعال/غیرفعال")
    categories = models.ManyToManyField(ProductCategory, blank=True, verbose_name='دسته بندی ها')
    visits = models.IntegerField(default=0, verbose_name="تعداد بازدید")

    objects = productManager()

    class Meta:
        verbose_name = "محصول"
        verbose_name_plural = "محصولات"

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return f"{self.id}/{self.title.replace(' ', '-')}"


class ProductGallery(models.Model):
    title = models.CharField(max_length=150, verbose_name="عنوان")
    image = models.ImageField(upload_to=setGalleryFileName, verbose_name="تصویر")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='محصول')

    class Meta:
        verbose_name = "تصویر"
        verbose_name_plural = "تصاویر"

    def __str__(self):
        return self.title
