# Generated by Django 3.1.3 on 2020-12-08 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdetail',
            name='count',
            field=models.IntegerField(verbose_name='تعداد'),
        ),
        migrations.AlterField(
            model_name='orderdetail',
            name='price',
            field=models.IntegerField(verbose_name='قیمت محصول'),
        ),
    ]
