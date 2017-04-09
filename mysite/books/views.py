from django.shortcuts import render
from books.models import Books


def search(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Please submit a search term.')
        elif len(q) > 20:
            errors.append('Please enter at most 20 characters')
        else:
            books = Books.objects.filter(title__icontains=q)
            return render(request, 'search_results.html',
                          {'books': books, 'query': q})
    return render(request, 'search_form.html', {'errors': errors})
