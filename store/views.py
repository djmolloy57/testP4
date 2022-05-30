from django.shortcuts import render
from . import forms
from .models import *

# Create your views here.
def designstore(request):
    products = Product.objects.all()
    context = { 'products':products }
    return render(request, 'store/designstore.html', context)

def sitelogin(request):
    context = {}
    return render(request, '../account.html', context)

# Create your views here.
def designstore2(request):
    context = {}
    return render(request, 'store/designstore2.html', context)

def cart(request):
    context = {}
    return render(request, 'store/cart.html', context)

def checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context)

def viewitem(request):
    context = {}
    return render(request, 'store/viewitem.html', context)

def form_name_view(request):
    form = forms.FormName()
    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
        
            print("VALIDATION SUCCESS!")
            print("NAME: " +form.cleaned_data['name'])
            print("EMAIL: "+form.cleaned_data['email'])
            print("TEXT: "+form.cleaned_data['text'])

    return render(request,'designstore/form_page.html', {'form': form})
