from django.urls import path

from shopify_bg.store.views import store, product_details, search

urlpatterns = (
    path('', store, name='store'),
    path('category/<slug:category_slug>/', store, name='products by category'),
    path('category/<slug:category_slug>/<slug:product_slug>/', product_details, name='product details'),
    path('search/', search, name='search'),
)