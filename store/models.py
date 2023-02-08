from django.db import models
from djmoney.models.fields import MoneyField
from django.urls import reverse

from category.models import Category

# Create your models here.


class Product(models.Model):
    product_name    = models.CharField(max_length=200, unique=True)
    slug            = models.SlugField(max_length=200, unique=True)
    description     = models.TextField(max_length=500, blank=True)
    price           = MoneyField(max_digits=19, decimal_places=2, default_currency='NGN')
    old_price       = MoneyField(max_digits=19, decimal_places=2, default_currency='NGN', null=True, blank=True)
    images          = models.ImageField(upload_to='photos/products')
    stock           = models.IntegerField()
    is_available    = models.BooleanField(default=True)
    category        = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now= True)
    
    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])
    
    def __str__(self):
        return self.product_name
    
