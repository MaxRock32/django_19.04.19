from django.shortcuts import render
from .models import ProductCategory, Product


def main(request):
    main_template = 'mainapp/index.html'
    main_context = {'user': {'name': 'reyborn_'},
                    'title': 'Main page',
                    'array': [1, 2, 3, 4, 5]}
    main_view = render(request=request,
                       template_name=main_template,
                       context=main_context)
    return main_view


def products(request):
    products_template = 'mainapp/products.html'
    products_context = {'products': Product.objects.all(),}
    products_view = render(request=request,
                           template_name=products_template,
                           context=products_context)
    return products_view


def contacts(request):
    contacts_template = 'mainapp/contacts.html'
    contacts_view = render(request=request,
                           template_name=contacts_template)
    return contacts_view

