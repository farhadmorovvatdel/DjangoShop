from django.shortcuts import render,redirect
from ProductModule.models import Categories,Products

def Home(request):

    return  render(request,"Home/Index.html")

def Header(request,title=None):
    categories=Categories.objects.prefetch_related('subcategory').only('title')
    # title=request.GET['title']
    # x=categories.filter(url_title=title)
    # print(x)

    context={
        'categories':categories,

         
    }
    return render(request,"shared/Header.html",context)


def Footer(request):
    return  render(request,"shared/Footer.html")





