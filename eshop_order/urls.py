from django.urls import path

from .views import *

urlpatterns = [
    path('add-user-order', addUserOrder),
    path('remove-order/<detailID>', remove_order_detail),
    path('open-order', userOpenOrder),
    # path('request', send_request, name='request'),
    # path('verify/<orderID>', verify, name='verify'),
]
