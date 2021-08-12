from django.db import models
import os


# Create your models here.

def setFileName(instance, file):
    base_name = os.path.basename(file)
    name, ext = os.path.splitext(base_name)
    final_name = f"{instance.title}{ext}"
    return f"logo-images/{final_name}"


class SiteSetting(models.Model):
    title = models.CharField(max_length=150, verbose_name="عنوان سایت")
    address = models.CharField(max_length=400, verbose_name="آدرس")
    phone = models.CharField(max_length=50, verbose_name="تلفن")
    mobile = models.CharField(max_length=50, verbose_name="تلفن همراه")
    fax = models.CharField(max_length=50, verbose_name="فکس")
    email = models.EmailField(max_length=50, verbose_name="ایمیل")
    about = models.TextField(verbose_name="درباره ی ما", null=True, blank=True)
    site_logo = models.ImageField(verbose_name="تصویر لوگو", upload_to=setFileName, blank=True, null=True)

    class Meta:
        verbose_name = "تنظیمات"
        verbose_name_plural = "تنظیمات سایت"

    def __str__(self):
        return self.title
