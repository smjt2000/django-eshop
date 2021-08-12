from django.db import models
from django.db.models.signals import pre_save, post_save
from .utiles import unique_slug_generator
from eshop_products.models import Product


# Create your models here.
class Tag(models.Model):
    title = models.CharField(max_length=120, verbose_name='عنوان')
    slug = models.SlugField(verbose_name='عنوان در url')
    timeStamp = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')
    active = models.BooleanField(default=True, verbose_name='فعال / غیرفعال')
    products = models.ManyToManyField(Product, blank=True, verbose_name='محصولات')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "برچسب"
        verbose_name_plural = "برچسب ها"


def tag_pre_save_reciver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(tag_pre_save_reciver, sender=Tag)
