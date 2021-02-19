from django.shortcuts import render
from Product.models import Product
from .models import *
# Create your views here.

def Home(request):
    settings = Settings.objects.get(id=1)
    slide_image = Product.objects.all().order_by('id')[:2]
    context = {'settings': settings, 'slide_image': slide_image}
    return render(request, 'home.html', context)