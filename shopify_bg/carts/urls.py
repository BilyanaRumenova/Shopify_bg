from django.urls import path

from shopify_bg.carts.views import cart, add_to_cart, remove_from_cart, remove_cart_item

urlpatterns = [
    path('', cart, name='cart'),
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add to cart'),
    path('remove_from_cart/<int:product_id>/<int:cart_item_id>/', remove_from_cart, name='remove from cart'),
    path('remove_cart_item/<int:product_id>/<int:cart_item_id>/', remove_cart_item, name='remove cart item'),
]