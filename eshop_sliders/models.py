from django.db import models
import os


# Create your models here.


def setFileName(instance, file):
    base_name = os.path.basename(file)
    name, ext = os.path.splitext(base_name)
    final_name = f"{instance.id}-{instance.title}{ext}"
    return f"sliders/images/{final_name}"


class Slider(models.Model):
    title = models.CharField(max_length=150, verbose_name='عنوان')
    link = models.URLField(max_length=100, verbose_name='آدرس')
    description = models.TextField(verbose_name='توضیحات')
    image = models.ImageField(upload_to=setFileName, blank=True, verbose_name='تصویر')

    class Meta:
        verbose_name = 'اسلایدر'
        verbose_name_plural = 'اسلایدرها'

    def __str__(self):
        return self.title
