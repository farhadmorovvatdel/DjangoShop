from django.urls import  path
from .views import ProdcutDetailView,ProductListView,ProductListFilter,AllProdcutList

app_name='products'
urlpatterns=[
    path('<url_title>/',ProductListView.as_view(),name='productlist'),
    path('',AllProdcutList.as_view(),name='AllProducts'),
    path('productdetail/<int:pk>/',ProdcutDetailView.as_view(),name='productdetail'),
    path('productfilter/<url_title>/',ProductListFilter,name='productfilter')
    # path('productcategory/<urltitle>',ProductCategoryListView.as_view(),name='prcategorylist'),

]