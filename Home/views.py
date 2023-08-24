from django.shortcuts import render,redirect
from ProductModule.models import Categories,Products

def Home(request):

    return  render(request,"Home/Index.html")

def Header(request):
    categories=Categories.objects.prefetch_related('subcategory').only('title')
    print(categories)
    context={
        'categories':categories,
    }
    return render(request,"shared/Header.html",context)


def Footer(request):
    return  render(request,"shared/Footer.html")





