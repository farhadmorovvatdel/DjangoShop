from django.db import models
from django.urls import reverse


class Categories(models.Model):
    title=models.CharField(max_length=20)
    url_title=models.CharField(max_length=20,db_index=True)
    parent=models.ForeignKey('self',null=True,blank=True,on_delete=models.CASCADE,related_name='subcategory')
    is_parent=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name='Category'
        verbose_name_plural='Categories'




class Products(models.Model):
    title=models.CharField(max_length=50,db_index=True)
    image=models.ImageField(upload_to='products/images',null=True,blank=True)
    description=models.TextField(null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    color = models.ForeignKey('Colors', on_delete=models.CASCADE,related_name='ProductColor',related_query_name='prcolor')
    capacity = models.ForeignKey('Capacity', on_delete=models.CASCADE,related_name='ProductCapacity',related_query_name='prcapcity')
    categories=models.ForeignKey('Categories',on_delete=models.CASCADE)
    price=models.CharField(max_length=20)
    count=models.PositiveSmallIntegerField(default=0)

    class Meta:
      verbose_name = 'Product'
      verbose_name_plural = 'Products'

    def __str__(self):
        return  f'{self.title}-{self.color}-{self.capacity}'

    def get_absolute_url(self):
        return reverse('products:productdetail',args={self.pk})








class Colors(models.Model):
    title=models.CharField(max_length=15)

    class Meta:
      verbose_name = 'Color'
      verbose_name_plural = 'Colors'

    def __str__(self):
        return self.title



class Capacity(models.Model):
    title = models.CharField(max_length=15)
    class Meta:
      verbose_name = 'Capacity'
      verbose_name_plural = 'Capacity'

    def __str__(self):
        return self.title


class ProductGalleries(models.Model):
    title = models.CharField(max_length=15)

    class Meta:
        verbose_name = 'ProductGallery'
        verbose_name_plural = 'ProductGallery'

    def __str__(self):
        return  self.title


