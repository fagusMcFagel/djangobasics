# \books\views.py
from django.shortcuts import render
from django.http.response import HttpResponse
from books.models import Book

## NOT NEEDED DUE TO UPDATED VIEW search(request) ##
#def search_form(request):
#    return render(request, 'books/search_form.html')

def search(request):
    error = False
    if 'q' in request.GET:
        q = request.GET['q']
        if q:
            books = Book.objects.filter(title__icontains=q)
            return render(request, 'books/search_results.html', 
                          {'books': books, 'query': q})
        else:
            error=True
    return render(request, 'books/search_form.html', {'error': error})