from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render,get_object_or_404,HttpResponse
from django.views.generic import  ListView,DetailView
import  json
from ProductModule.models import Products,Categories




class ProductListView(ListView):
     template_name = 'Products/ProductList.html'
     model = Products
     def get_queryset(self,*args,**kwars):

          url_title=self.kwargs['url_title']
          query= super().get_queryset().filter(categories__url_title=url_title)
          return  query
     def get_context_data(self,*args,**kwargs):
         context=super().get_context_data(*args,**kwargs)
         context['categories']=Categories.objects.filter(is_parent=True)

         return context


def ProductCategory(request):
    url_title=request.GET.get('url_title')
    products=Products.objects.filter(categories__url_title=url_title)
    context={
        'products':products
    }
    return render(request)




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
    model =Products


# class ProductListFilter(ListView):
#     template_name = 'Products/ProductListPartial.html'
#     model = Products
#     def get_queryset(self,*args,**kwargs):
#         q=self.kwargs['catname']
#         print(q)
#         query=super(ProductListFilter, self).get_queryset().filter(
#             categories__parent_id=q
#         )
#         print(query)
#         return query
#



