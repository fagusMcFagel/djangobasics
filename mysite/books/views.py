# \books\views.py
from django.shortcuts import render
from django.http.response import HttpResponse
from books.models import Book

## NOT NEEDED DUE TO UPDATED VIEW search(request) ##
#def search_form(request):
#    return render(request, 'books/search_form.djhtml')

#===============================================================================
# earlier version with error as boolean -> unspecific error messages
# def search(request):
#     error=False
#     if 'q' in request.GET:
#         q = request.GET['q']
#         if not q:
#             error=True
#         elif len(q)>20:
#             error=True
#         else:
#             books = Book.objects.filter(title__icontains=q)
#             return render(request, 'books/search_results.djhtml', 
#                           {'books': books, 'query': q})
#     return render(request, 'books/search_form.djhtml', {'errors': errors})
#===============================================================================

def search(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Enter a search term.')
        elif len(q)>20:
            errors.append('Please enter at most 20 characters.')
        else:
            books = Book.objects.filter(title__icontains=q)
            return render(request, 'books/search_results.djhtml', 
                          {'books': books, 'query': q})
    return render(request, 'books/search_form.djhtml', {'errors': errors})