from django.urls import path
from eshop_products.views import *

urlpatterns = [
    path('products', Products),
    path('products/', Products),
    path('products/<category_name>', ProductsByCategory.as_view()),
    path('products/<ID>/', product_detail),
    path('products/<ID>/<title>', product_detail),
    path('products/search', searchProducts.as_view()),
    path('products_categories_partial', ProductsCategoryPartial, name="products_categories_partial"),
]
