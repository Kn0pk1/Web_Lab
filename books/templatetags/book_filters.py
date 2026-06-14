from django import template
from django.utils.safestring import mark_safe

register = template.Library()

# 1. Скрывает ISBN (показывает только последние 4 цифры)
@register.filter
def hide_isbn(value):
    if value and len(value) > 4:
        return f"...{value[-4:]}"
    return value or "—"

# 2. Возраст книги с иконками
@register.filter
def book_age(year):
    from datetime import datetime
    current_year = datetime.now().year
    try:
        y = int(year)
        if y >= current_year - 1:
            return mark_safe('<i class="fas fa-star"></i> Новинка')
        elif y <= current_year - 10:
            return mark_safe('<i class="fas fa-book"></i> Классика')
        else:
            return mark_safe('<i class="fas fa-leaf"></i> Современная')
    except (TypeError, ValueError):
        return "—"

# 3. Ценовая категория с иконками
@register.filter
def price_level(price):
    try:
        p = float(price)
        if p < 500:
            return mark_safe('<i class="fas fa-coffee"></i> Бюджетная')
        elif p < 1500:
            return mark_safe('<i class="fas fa-utensils"></i> Средняя')
        elif p < 3000:
            return mark_safe('<i class="fas fa-gem"></i> Выше среднего')
        else:
            return mark_safe('<i class="fas fa-crown"></i> Дорогая')
    except (TypeError, ValueError):
        return "—"