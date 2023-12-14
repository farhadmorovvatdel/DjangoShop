from typing import Any
from django.db.models.query import QuerySet
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
         context['categories']=Categories.objects.filter(is_parent=True)

         return context




class ProdcutDetailView(DetailView):
    template_name = 'Products/Prodcut_Detail.html'
    model =Products



def ProductListFilter(request,url_title):
    productfilter=Products.objects.filter(categories__is_parent=False,categories__url_title='سامسونگ').all()
    print(productfilter)

    context={
        'Products':productfilter
    }
    return render(request,'Products/ProductList.html',context)





