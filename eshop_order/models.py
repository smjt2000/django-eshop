from django.db import models

from django.contrib.auth.models import User

# Create your models here.
from eshop_products.models import Product


class Order(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    is_paid = models.BooleanField(verbose_name="پرداخت شده / نشده")
    payment_date = models.DateTimeField(blank=True, null=True, verbose_name="تاریخ پرداخت")
    refID = models.CharField(verbose_name="کد پیگیری", max_length=150, null=True, blank=True)

    class Meta:
        verbose_name = "سبد خرید"
        verbose_name_plural = "سبد های خرید کاربران"

    def __str__(self):
        return self.owner.get_full_name()

    def total_price(self):
        amount = 0
        for detail in self.orderdetail_set.all():
            amount += detail.price * detail.count
        return amount


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name="سبد خرید")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="محصول")
    price = models.IntegerField(verbose_name="قیمت محصول")
    count = models.IntegerField(verbose_name="تعداد")

    def order_sum(self):
        return self.count * self.price

    class Meta:
        verbose_name = "جزییات محصول"
        verbose_name_plural = "اطلاعات جزییات محصول"

    def __str__(self):
        return self.product.title
