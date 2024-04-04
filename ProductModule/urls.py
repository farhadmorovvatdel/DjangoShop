from django.urls import  path
from .views import ProdcutDetailView,ProductListView,AllProdcutList,ProductListFilter,ProductListFilterPrice

app_name='products'
urlpatterns=[
    path('<url_title>/',ProductListView.as_view(),name='productlist'),
    path('',AllProdcutList.as_view(),name='AllProducts'),
    path('productdetail/<int:pk>/',ProdcutDetailView.as_view(),name='productdetail'),
    path('filter/<url_title>/',ProductListFilter,name='productfilter'),
    path('filterprice',ProductListFilterPrice,name='productfilterprice'),



]