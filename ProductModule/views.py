from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render,get_object_or_404
from django.views.generic import  ListView,DetailView
import  json
from ProductModule.models import Products,Categories


class ProductListView(ListView):
     template_name = 'Products/ProductList.html'
     
     def get_queryset(self,*args,**kwars):
          url_title=self.kwargs['url_title']
          query= super().get_queryset()
          query.filter(url__title=url_title)
          return query






     # def get_context_data(self, *, object_list=None, **kwargs):
     #     context=super(ProductListView, self).get_context_data(**kwargs)
     #     products=Categories.objects.prefetch_related('products_set')
     #     context['products']=products
     #     return context

# class ProductCategoryListView(ListView):
#     template_name = 'Products/ProductCategory.html'
#     context_object_name = 'productcategory'
#     def get_queryset(self,**kwargs):
#         urltittle=self.kwargs['urltitle']
#         query=Products.objects.filter(categories__url_title=urltittle)
#         # if query is None:
#         #     return  render(request,'shared/404.html')
#         # else:
#         # print(query)
#         return query
#     def get_context_data(self, *, object_list=None, **kwargs):
#         request=self.request
#         x=request.GET.get('data')
#         print(x)
#         context=super(ProductCategoryListView, self).get_context_data(**kwargs)
#         context['categories']=Categories.objects.filter(is_parent=True).only('title')
#         # print(context)
#         return context

class ProdcutDetailView(DetailView):
    template_name = 'Products/Prodcut_Detail.html'
    model = Products






