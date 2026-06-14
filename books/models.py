from django.db import models


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