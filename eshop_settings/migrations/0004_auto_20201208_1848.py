# Generated by Django 3.1.3 on 2020-12-08 18:48

from django.db import migrations, models
import eshop_settings.models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_settings', '0003_auto_20201208_1101'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sitesetting',
            options={'verbose_name': 'تنظیمات', 'verbose_name_plural': 'تنظیمات سایت'},
        ),
        migrations.AddField(
            model_name='sitesetting',
            name='site_logo',
            field=models.ImageField(blank=True, null=True, upload_to=eshop_settings.models.setFileName, verbose_name='تصویر لوگو'),
        ),
    ]