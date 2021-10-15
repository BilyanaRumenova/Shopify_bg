from django.contrib import admin

from shopify_bg.store.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'stock', 'category', 'date_created', 'date_modified', 'is_available',)
    prepopulated_fields = {'slug': ('product_name',)}


