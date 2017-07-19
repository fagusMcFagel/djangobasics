# \books\views.py
from django.shortcuts import render
from django.http.response import HttpResponse
from books.models import Book

def search_form(request):
    return render(request, 'books/search_form.html')

def search(request):
    if 'q' in request.GET:
        q = request.GET['q']
        books = Book.objects.filter(title__icontains=q)
        return render(request, 'books/search_results.html', 
                      {'books': books, 'query': q})
    else:
        return HttpResponse('Please enter a search term')