from typing import Any
from django.db.models.query import QuerySet
from django.core import serializers
from django.http import  JsonResponse
from django.shortcuts import render,get_object_or_404,HttpResponse
from django.views.generic import  ListView,DetailView
import  json
from ProductModule.models import Products,Categories

class AllProdcutList(ListView):
    template_name = 'Products/AllProdcutList.html'
    model = Products
    paginate_by = 2
    def get_queryset(self):
        return super(AllProdcutList, self).get_queryset()
    def get_context_data(self, *args,**kwargs):
        context=super(AllProdcutList, self).get_context_data(*args,**kwargs)
        context['categories'] = Categories.objects.filter(is_parent=False)

        return  context





class ProductListView(ListView):
     template_name = 'Products/ProductList.html'
     model = Products
     paginate_by = 2
     def get_queryset(self,*args,**kwars):

          url_title=self.kwargs['url_title']
          query= super().get_queryset().filter(categories__url_title=url_title)
          return  query
     def get_context_data(self,*args,**kwargs):
         context=super().get_context_data(*args,**kwargs)
         context['categories']=Categories.objects.filter(is_parent=False)


         return context




class ProdcutDetailView(DetailView):
    template_name = 'Products/Prodcut_Detail.html'
    model =Products



def ProductListFilter(request,url_title):
    productfilter=list(Products.objects.filter(categories__url_title=url_title).values())
    print(productfilter)
    return  JsonResponse(productfilter,safe=False)
    # serializer = serializers.serialize('json',productfilter)
    # data={
    #     'queryset':serializer
    # }
    # print(data)
    # return JsonResponse({
    #     'data':serializer
    # })
def ProductListFilterPrice(request):
    t=request.GET.get('test')
    print(t)
    filterprice=Products.objects.values_list('price',flat=True)

    context={
    'filterprice':filterprice
    }
    return render(request,'Products/CatgoriesFilter.html',context)


