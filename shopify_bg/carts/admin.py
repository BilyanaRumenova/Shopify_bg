from django.contrib import admin

from shopify_bg.carts.models import Cart, CartItem

admin.site.register(Cart)

admin.site.register(CartItem)
