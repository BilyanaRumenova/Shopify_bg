from django.db import models


class Category(models.Model):
    TYPE_CHOICE_JACKETS = 'jackets'
    TYPE_CHOICE_JEANS = 'jeans'
    TYPE_CHOICE_SHIRTS = 'shirts'
    TYPE_CHOICE_SHOES = 'shoes'
    TYPE_CHOICE_T_SHIRTS = 't-shirts'

    TYPE_CHOICES = (
        (TYPE_CHOICE_JACKETS, 'Jackets'),
        (TYPE_CHOICE_JEANS, 'Jeans'),
        (TYPE_CHOICE_SHIRTS, 'Shirts'),
        (TYPE_CHOICE_SHOES, 'Shoes'),
        (TYPE_CHOICE_T_SHIRTS, 'T-Shirts'),
    )

    category_name = models.CharField(max_length=50, unique=True, choices=TYPE_CHOICES,)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=250, blank=True)
    category_image = models.ImageField(upload_to='photos/categories', blank=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.category_name