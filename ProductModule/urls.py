from django.urls import  path
from .views import ProdcutDetailView

app_name='products'
urlpatterns=[
    # path('<url_title>/',ProductListView.as_view(),name='productlist'),
    path('productdetail/<int:pk>/',ProdcutDetailView.as_view(),name='productdetail'),
    # path('productcategory/<urltitle>',ProductCategoryListView.as_view(),name='prcategorylist'),

]