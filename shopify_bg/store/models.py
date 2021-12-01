from django.db import models
from django.urls import reverse

from shopify_bg.category.models import Category
from shopify_bg.store.managers import VariationManager


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

    def get_url(self):
        return reverse('product details', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.product_name


class Variation(models.Model):
    TYPE_CHOICE_COLOUR = 'colour'
    TYPE_CHOICE_SIZE = 'size'

    VARIATION_CATEGORY_CHOICES = (
        (TYPE_CHOICE_COLOUR, 'colour'),
        (TYPE_CHOICE_SIZE, 'size'),
    )

    product = models.ForeignKey(Product, models.CASCADE)
    variation_category = models.CharField(max_length=100, choices=VARIATION_CATEGORY_CHOICES, )
    variation_value = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now=True)

    objects = VariationManager()

    def __str__(self):
        return self.variation_value



