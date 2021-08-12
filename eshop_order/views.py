import time
from typing import re

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
# from zeep import Client

# Create your views here.
from eshop_products.models import Product
from .forms import OrderForm
from .models import Order, OrderDetail


@login_required(login_url="/login")
def addUserOrder(request):
    order_forms = OrderForm(request.POST or None)

    if order_forms.is_valid():
        order = Order.objects.filter(owner_id=request.user.id, is_paid=False).first()
        if order is None:
            order = Order.objects.create(owner_id=request.user.id, is_paid=False)

        product_id = order_forms.cleaned_data.get("productID")
        count = order_forms.cleaned_data.get("count")
        if count < 0:
            count = 1
        product = Product.objects.get(id=product_id)
        check = 0
        for detail in OrderDetail.objects.all():
            if detail.product_id == product.id:
                count += detail.count
                detail.delete()
                check = 1

        order.orderdetail_set.create(product_id=product.id, price=product.price, count=count)
        return redirect(f'/products/{product.id}/{product.title.replace(" ", "-")}')


@login_required(login_url="/login")
def userOpenOrder(request):
    context = {
        "title": "سبد خرید",
        "order": None,
        "details": None,
        "total": 0
    }
    open_order: Order = Order.objects.filter(owner_id=request.user.id, is_paid=False).first()
    if open_order is not None:
        context["order"] = open_order
        context["details"] = open_order.orderdetail_set.all()
        context["total"] = open_order.total_price()

    return render(request, "user_open_order.html", context)


@login_required(login_url="/login")
def remove_order_detail(request, detailID):
    if detailID is not None:
        order_detail = OrderDetail.objects.get_queryset().get(id=detailID, order__owner_id=request.user.id)
        if order_detail is not None:
            order_detail.delete()
    return redirect("/open-order")


# ##########################
"""
payment settings
"""
# ##########################


# MERCHANT = 'XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX'
# client = Client('https://www.zarinpal.com/pg/services/WebGate/wsdl')
# amount = 1000  # Toman / Required
# description = "توضیحات مربوط به تراکنش را در این قسمت وارد کنید"  # Required
# email = 'email@example.com'  # Optional
# mobile = '09123456789'  # Optional
# CallbackURL = 'http://localhost:8000/verify/'  # Important: need to edit for realy server.
#


# def send_request(request):
#     total_price = 0
#
#     open_order: Order = Order.objects.filter(is_paid=False, owner_id=request.user.id).first()
#     if open_order is not None:
#         total_price = open_order.total_price()
#
#         result = client.service.PaymentRequest(MERCHANT, total_price, description, email, mobile,
#                                                f"{CallbackURL}{open_order.id}")
#         if result.Status == 100:
#             return redirect('https://www.zarinpal.com/pg/StartPay/' + str(result.Authority))
#         else:
#             return HttpResponse('Error code: ' + str(result.Status))
#
#     raise Http404()
#
#
# def verify(request, orderID=None):
#     if request.GET.get('Status') == 'OK':
#         result = client.service.PaymentVerification(MERCHANT, request.GET['Authority'], amount)
#         if result.Status == 100:
#             user_order = Order.objects.get_queryset().get(id=orderID)
#             user_order.is_paid = True
#             user_order.payment_date = time.time()
#             user_order.refID = result.RefID
#             user_order.save()
#
#             return HttpResponse('Transaction success.\nRefID: ' + str(result.RefID))
#         elif result.Status == 101:
#             return HttpResponse('Transaction submitted : ' + str(result.Status))
#         else:
#             return HttpResponse('Transaction failed.\nStatus: ' + str(result.Status))
#     else:
#         return HttpResponse('Transaction failed or canceled by user')
