from django.urls import  path
from .views import ProductListView,ProductCategoryListView

app_name='products'
urlpatterns=[
    path('',ProductListView.as_view(),name='productlist'),
    path('productcategory/<urltitle>',ProductCategoryListView.as_view(),name='prcategorylist')
]