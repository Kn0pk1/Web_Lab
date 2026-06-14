from django.db import models
from django.core.exceptions import ValidationError

class Book(models.Model):
    title = models.CharField(max_length=300, verbose_name="Название")
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name="Цена")
    author = models.CharField(max_length=200, blank=True, null=True, verbose_name="Автор")
    city = models.CharField(max_length=100, blank=True, null=True, verbose_name="Город")
    source = models.CharField(max_length=100, blank=True, null=True, verbose_name="Источник")
    isbn = models.CharField(max_length=50, blank=True, null=True, verbose_name="ISBN")
    publisher = models.CharField(max_length=200, blank=True, null=True, verbose_name="Издательство")
    year = models.CharField(max_length=10, blank=True, null=True, verbose_name="Год")
    genre = models.CharField(max_length=200, blank=True, null=True, verbose_name="Жанр")
    isbn_clean = models.CharField(max_length=20, blank=True, null=True, verbose_name="ISBN (чистый)")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления")

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
        ordering = ['-created_at']

    def __str__(self):
        return self.title

class Customer(models.Model):
    name = models.CharField(max_length=200, verbose_name="Имя покупателя")
    email = models.EmailField(blank=True, null=True, verbose_name="Email")
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name="Телефон")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата регистрации")

    class Meta:
        verbose_name = "Покупатель"
        verbose_name_plural = "Покупатели"

    def __str__(self):
        return self.name

class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="carts", verbose_name="Покупатель")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    is_active = models.BooleanField(default=True, verbose_name="Активна")
    books = models.ManyToManyField(Book, verbose_name="Товары")

    class Meta:
        verbose_name = "Корзина"
        verbose_name_plural = "Корзины"
        constraints = [
            models.UniqueConstraint(
                fields=['customer', 'is_active'],
                condition=models.Q(is_active=True),
                name='unique_active_cart_per_customer'
            )
        ]

    def clean(self):
        if self.is_active:
            existing_active = Cart.objects.filter(customer=self.customer, is_active=True).exclude(pk=self.pk)
            if existing_active.exists():
                raise ValidationError('У этого покупателя уже есть активная корзина.')

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Корзина #{self.id} - {self.customer.name}"
