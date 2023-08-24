from django.shortcuts import render
from django.views.generic import  ListView

from ProductModule.models import Products,Categories


class ProductListView(ListView):
     template_name = 'Products/ProductList.html'
     def get_queryset(self):
         query=Products.objects.all()
         return query

     # def get_context_data(self, *, object_list=None, **kwargs):
     #     context=super(ProductListView, self).get_context_data(**kwargs)
     #     products=Categories.objects.prefetch_related('products_set')
     #     context['products']=products
     #     return context

class ProductCategoryListView(ListView):
    template_name = 'Products/ProductCategory.html'
    context_object_name = 'productcategory'
    def get_queryset(self,**kwargs):
        urltittle=self.kwargs['urltitle']
        query=Products.objects.filter(categories__url_title=urltittle)
        print(query)
        return query
    def get_context_data(self, *, object_list=None, **kwargs):
        context=super(ProductCategoryListView, self).get_context_data(**kwargs)
        context['categories']=Categories.objects.filter(is_parent=True).only('title')
        return context
