from django.contrib import admin
from .models import Product, Order, Client


# Register your models here.

@admin.action(description='Поставка продукта (+100)')
def add_quantity(ModelAdmin, request, queryset):
    queryset.update(quantity=100)


@admin.action(description='Обнуление продукта')
def zeroing_product(ModelAdmin, request, queryset):
    queryset.update(name=None, description=None, price=None, quantity=None, date_add_product=None, image=None)


class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'number_phone', 'date_registration']
    list_filter = ['name', 'date_registration']
    search_fields = ['number_phone']
    fieldsets = [(
        'Общая информация',
        {
            'fields': ['name', 'number_phone', 'address']
        }
    ), (
        'Информация для внутренней системы',
        {
            'fields': ['email', 'date_registration']
        }
    )]


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'quantity']
    list_filter = ['name', 'price']
    search_fields = ['name']
    actions = [add_quantity, zeroing_product]
    fieldsets = [(
        'Общая информация',
        {
            'fields': ['name', 'price', 'description', 'image']
        }
    ), (
        'Информация для внутренней системы',
        {
            'fields': ['quantity', 'date_add_product']
        }
    )]


class OrderAdmin(admin.ModelAdmin):
    list_display = ['client', 'product', 'sum_of_order']
    list_filter = ['client', 'product', 'date_order']
    search_fields = ['client', 'sum_of_order', 'date_order']
    fieldsets = [(
        'Общая информация',
        {
            'fields': ['client', 'product', 'sum_of_order']
        }
    ), (
        'Информация для внутренней системы',
        {
            'fields': ['date_order']
        }
    )
    ]


admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
admin.site.register(Client, ClientAdmin)
