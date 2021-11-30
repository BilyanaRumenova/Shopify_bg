from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect, get_object_or_404

from shopify_bg.carts.models import Cart, CartItem
from shopify_bg.store.models import Product


def _get_cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart


def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id) #get the product
    try:
        cart = Cart.objects.get(cart_id=_get_cart_id(request))  #get the cart using the cart_id present in the session
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id=_get_cart_id(request)
        )
    cart.save()

    try:
        cart_item = CartItem.objects.get(
            product=product,
            cart=cart
        )
        cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            product=product,
            quantity=1,
            cart=cart,
        )
        cart_item.save()
    return redirect('cart')


def remove_from_cart(request, product_id):
    cart = Cart.objects.get(cart_id=_get_cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()

    return redirect('cart')


def remove_cart_item(request, product_id):
    cart = Cart.objects.get(cart_id=_get_cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    cart_item.delete()
    return redirect('cart')


def cart(request, total_price=0, quantity=0, cart_items=None):
    tax = 0
    grand_total_price = 0
    try:
        cart = Cart.objects.get(cart_id=_get_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, is_active=True)
        for cart_item in cart_items:
            quantity += cart_item.quantity
            total_price += (cart_item.product.price * cart_item.quantity)

        tax = (2 * total_price) / 100
        grand_total_price = total_price + tax
    except Exception:
        raise ObjectDoesNotExist

    context = {
        'total_price': total_price,
        'quantity': quantity,
        'cart_items': cart_items,
        'tax': tax,
        'grand_total_price': grand_total_price,
    }
    return render(request, 'store/cart.html', context)



