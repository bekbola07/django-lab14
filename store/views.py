from django.shortcuts import render, redirect
from .models import *
from .forms import ChoiseForm
def home(request):
    ctg = Category.objects.all()
    product = Product.objects.all()
    ctx={'ctg':ctg,
         'product':product }
    return render(request,'index.html',ctx)
def contact(request):
    ctx={}
    return render(request,'contact.html',ctx)
def products(request, slug=None):
    ctg = Category.objects.all()
    category = Category.objects.get(slug=slug)
    product = Product.objects.all().filter(type_id=category.id)
    ctx={'ctg':ctg,
         'category':category,
         'product':product}
    return render(request,'products.html',ctx)
def register(request):
    ctx={}
    return render(request,'register.html',ctx)
def single(requests, pk=None):
    ctg = Category.objects.all()
    product_pk = Product.objects.get(pk=pk)
    form = ChoiseForm()
    if requests.POST:
        forms = ChoiseForm(requests.POST or None,
                           requests.FILES or None)
        if forms.is_valid():
            root=forms.save()
            root=Buy.objects.get(pk=root.pk)
            root.product=product_pk
            root.save()
            return redirect('home')
        else:
            print(forms.errors)

    ctx={'ctg': ctg,
         'product_pk':product_pk,
         'form':form}
    return render(requests,'single.html',ctx)