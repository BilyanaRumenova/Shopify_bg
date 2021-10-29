from django.urls import path

from shopify_bg.store.views import store, product_details

urlpatterns = (
    path('', store, name='store'),
    path('<slug:category_slug>/', store, name='products by category'),
    path('<slug:category_slug>/<slug:product_slug>/', product_details, name='product details'),
)