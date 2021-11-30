from shopify_bg.carts.models import CartItem, Cart
from shopify_bg.carts.views import _get_cart_id


def counter(request):
    cart_items_count = 0
    if 'admin' in request.path:
        return {}
    else:
        try:
            cart = Cart.objects.filter(cart_id=_get_cart_id(request))
            cart_items = CartItem.objects.all().filter(cart=cart[0])
            for cart_item in cart_items:
                cart_items_count += cart_item.quantity
        except Cart.DoesNotExist:
            cart_items_count = 0

    return dict(cart_items_count=cart_items_count)