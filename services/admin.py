from django.contrib import admin
from .models import Product, Basket

#admin.site.register(Product)
#admin.site.register(Basket)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'cost']
    list_editable = ['cost']
    # fields = ['id']
    list_filter = ['cost']
    search_fields = ['title']
    ordering = ['id']
    list_per_page = 4


#admin.site.register(Product, ProductAdmin)

@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    list_display = ['title', 'cost']
    list_editable = ['cost']
    # fields = ['id']
    list_filter = ['cost']
    search_fields = ['title']
    ordering = ['id']
    list_per_page = 4