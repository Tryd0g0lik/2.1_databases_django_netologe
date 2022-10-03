import random
from django.shortcuts import render, redirect
from PIL import Image

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    sort_name = request.GET.get('sort')
    if sort_name == 'name': # , 'min_price', 'max_price']
      product_object = Phone.objects.all().order_by('name')
    elif sort_name == 'min_price':
      product_object = Phone.objects.all().order_by('price')
    elif sort_name == 'max_price':
      product_object = Phone.objects.all().order_by('-price')
    else:
      product_object = Phone.objects.all()

    template = 'catalog.html'
    phones = [p for p in product_object]

    return render(request=request,
                  template_name=template,
                  context={'phones' : phones})



def show_product(request, slug):
    template = 'product.html'
    context = {}
    return render(request, template, context, )

