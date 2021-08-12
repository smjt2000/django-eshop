import itertools

from django.http import Http404
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.views.generic import ListView

from eshop_order.forms import OrderForm
from eshop_products_category.models import ProductCategory

from .models import *


# Create your views here.

def Products(request):
    products = Product.objects.filter(active=True)
    item_per_page = 3
    paginator = Paginator(products, item_per_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    page_range = products.count() // item_per_page
    if (products.count() / item_per_page) > page_range:
        page_range += 1
    page_range = range(1, page_range + 1)
    context = {
        "title": "محصولات",
        "page_obj": page_obj,
        "page_range": page_range,
    }
    return render(request, "products_list.html", context)


def my_grouper(n, iterable):
    args = [iter(iterable)] * n
    return ([e for e in t if e is not None] for t in itertools.zip_longest(*args))


def product_detail(request, ID, title=None):
    product = Product.objects.filter(id=ID)

    if product.count() == 1:
        product = product.first()
    else:
        raise Http404("محصول موردنظر یافت نشد")

    if not product.active:
        raise Http404("محصول موردنظر یافت نشد")

    product.visits += 1
    product.save()

    order_forms = OrderForm(request.POST or None, initial={'productID': product.id})

    related_products = Product.objects.get_queryset().filter(categories__product=product).distinct()

    grouped_related_products = my_grouper(3, related_products)

    galleries = ProductGallery.objects.filter(product_id=product)

    grouped_galleries = list(my_grouper(3, galleries))

    context = {
        "title": product.title,
        "product": product,
        "galleries": grouped_galleries,
        "related_products": grouped_related_products,
        "order_form": order_forms,
    }
    if title == None or title != product.title.replace(' ', '-'):
        return redirect(f"/products/{ID}/{product.title.replace(' ', '-')}")

    return render(request, "product_detail.html", context)


class searchProducts(ListView):
    paginate_by = 3
    template_name = "products_list.html"

    def get_queryset(self):
        request = self.request
        query = request.GET.get('q')
        if query is not None:
            return Product.objects.search(query)
        return Product.objects.filter(active=True)


class ProductsByCategory(ListView):
    template_name = 'products_list.html'
    paginate_by = 6

    def get_queryset(self):
        category_name = self.kwargs['category_name']
        category = ProductCategory.objects.filter(name__iexact=category_name).first()
        if category is None:
            raise Http404('صفحه ی مورد نظر یافت نشد')
        return Product.objects.product_by_category(category_name)


def ProductsCategoryPartial(request):
    categories = ProductCategory.objects.all()
    context = {
        "categories": categories,
    }
    return render(request, "products_categories.html", context)
