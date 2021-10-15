from django.db import models

from shopify_bg.category.models import Category


class Product(models.Model):
    product_name = models.CharField(max_length=200, unique=True,)
    slug = models.SlugField(max_length=200, unique=True,)
    description = models.TextField(max_length=500, blank=True)
    price = models.IntegerField()
    image = models.ImageField(upload_to='photos/products')
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name