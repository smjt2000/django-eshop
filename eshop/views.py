import itertools

from django.shortcuts import render, redirect

from eshop_products.models import Product
from eshop_sliders.models import Slider
from eshop_settings.models import SiteSetting


def header(request, *args, **kwargs):
    context = {}
    return render(request, 'base/header.html', context)


def footer(request, *args, **kwargs):
    site_setting = SiteSetting.objects.first()
    context = {
        "setting": site_setting,
    }
    return render(request, 'base/footer.html', context)


def my_grouper(n, iterable):
    args = [iter(iterable)] * n
    return ([e for e in t if e is not None] for t in itertools.zip_longest(*args))


def home_page(request):
    most_visited_products = Product.objects.order_by('-visits').all()[:8]
    latest_products = Product.objects.order_by('-id').all()[:8]
    sliders = Slider.objects.all()
    context = {
        "title": "صفحه اصلی",
        "sliders": sliders,
        "most_visited": my_grouper(4, most_visited_products),
        "latest_prodcucts": my_grouper(4, latest_products),
    }
    return render(request, "home_page.html", context)


def about_page(request):
    site_setting = SiteSetting.objects.first()
    context = {
        "title": "درباره ما",
        "setting": site_setting,
    }
    return render(request, "about_page.html", context)
