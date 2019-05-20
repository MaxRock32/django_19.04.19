from django.shortcuts import render, get_object_or_404
from mainapp.models import ProductCategory, Product
from basketapp.models import Basket


def get_user_basket(user):
    return Basket.objects.filter(user=user) if user.is_authenticated else []


def get_common_context(request):
    common_context = {}
    if get_user_basket(request.user):
        common_context = {
            'basket': get_user_basket(request.user),
            'products_total_quantity': get_user_basket(request.user)[0].get_products_total_quantity_by_user,
            'products_total_price': get_user_basket(request.user)[0].get_products_total_price_by_user,
        }
    return common_context


def get_hot_product():
    return Product.objects.all().order_by('?').first()


def get_same_products(hot_product):
    return Product.objects.filter(category=hot_product.category).exclude(pk=hot_product.pk)[:3]


def main(request):
    context = {
        'page_title': 'Interior - main',
        'products': Product.objects.all().order_by('?')[:4],
        **get_common_context(request),
    }
    return render(request, 'mainapp/index.html', context)


def products(request, pk=None):
    page_title = 'Interior - products'

    links_menu = ProductCategory.objects.all()
    if pk:
        if pk == '0':
            products = Product.objects.all().order_by('price')
            category = {'name': 'ALL'}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk).order_by('price')

        context = {
            'page_title': page_title,
            'links_menu': links_menu,
            'category': category,
            'products': products,
            **get_common_context(request),
        }

        return render(request, 'mainapp/products_list.html', context)

    context = {
        'page_title': page_title,
        'links_menu': links_menu,
        **get_common_context(request),
    }

    return render(request, 'mainapp/products.html', context)


def contacts(request):
    context = {
        'page_title': 'Interior - contacts',
        **get_common_context(request),
    }
    return render(request, 'mainapp/contacts.html', context)


def showroom(request):
    hot_product = get_hot_product()

    context = {
        'page_title': 'Interior - showroom',
        'links_menu': ProductCategory.objects.all(),
        'hot_product': hot_product,
        'same_products': get_same_products(hot_product),
        **get_common_context(request),
    }
    return render(request, 'mainapp/showroom.html', context)


def product_details(request, pk):
    context = {
        'page_title': 'Interior - product details',
        'links_menu': ProductCategory.objects.all(),
        'detailed_product': get_object_or_404(Product, pk=pk),
        **get_common_context(request),
    }
    return render(request, 'mainapp/product-details.html', context)
