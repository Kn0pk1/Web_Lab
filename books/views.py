from django.shortcuts import render, get_object_or_404
from .models import Book, Cart


def book_list(request):
    query = request.GET.get('q', '')
    books = Book.objects.all()

    if query:
        query_lower = query.lower()
        all_books = list(books)
        filtered = []
        for book in all_books:
            if query_lower in book.title.lower() or query_lower in (book.author or '').lower():
                filtered.append(book)

        filtered.sort(key=lambda b: (
            0 if b.title.lower().startswith(query_lower) else 1,
            b.title.lower()
        ))
        books = filtered

    return render(request, 'books/book_list.html', {'books': books, 'query': query})

def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'books/book_detail.html', {'book': book})

def carts_list(request):
    carts = Cart.objects.all().select_related('customer').prefetch_related('books')
    return render(request, 'books/carts.html', {'carts': carts})