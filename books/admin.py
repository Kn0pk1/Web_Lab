from django.contrib import admin
from .models import Book, Customer, Cart

class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'price', 'source']
    search_fields = ['title', 'author']

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'created_at']
    search_fields = ['name', 'email']


class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'created_at', 'is_active']
    list_filter = ['is_active', 'created_at']
    search_fields = ['customer__name']
    filter_horizontal = ['books']
    readonly_fields = ['created_at']


admin.site.register(Book, BookAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Cart, CartAdmin)
