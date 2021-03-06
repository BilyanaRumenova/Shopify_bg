from django.contrib import admin

from shopify_bg.category.models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category_name',)}
    list_display = ('category_name', 'slug',)

# admin.site.register(Category)

