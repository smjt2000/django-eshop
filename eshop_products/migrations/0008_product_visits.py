# Generated by Django 3.1.3 on 2020-12-09 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_products', '0007_auto_20201207_1606'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='visits',
            field=models.IntegerField(default=0, verbose_name='تعداد بازدید'),
        ),
    ]
