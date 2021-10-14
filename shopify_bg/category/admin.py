from django.contrib import admin

from shopify_bg.category.models import Category


admin.site.register(Category)

# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('category_name',)
