from django.contrib import admin
from .models import Book, Customer, Cart, CartItem

class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'price', 'source']
    search_fields = ['title', 'author']

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'created_at']
    search_fields = ['name', 'email']


class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 1
    autocomplete_fields = ['book']
    fields = ['book', 'quantity']


class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'created_at', 'is_active', 'total_items_count_display', 'total_price_display']
    list_filter = ['is_active', 'created_at']
    search_fields = ['customer__name']
    inlines = [CartItemInline]
    readonly_fields = ['created_at', 'total_items_count_display', 'total_price_display']
    date_hierarchy = 'created_at'

    fieldsets = (
        (None, {
            'fields': ('customer', 'is_active')
        }),
        ('Вычисления', {
            'fields': ('total_items_count_display', 'total_price_display'),
            'classes': ('collapse',)
        }),
        ('Дополнительно', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )

    def total_items_count_display(self, obj):
        return obj.total_items_count()

    total_items_count_display.short_description = "Всего единиц"

    def total_price_display(self, obj):
        return f"{obj.total_price():.2f} ₽"

    total_price_display.short_description = "Итоговая стоимость"

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('items__book')


admin.site.register(Book, BookAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem)