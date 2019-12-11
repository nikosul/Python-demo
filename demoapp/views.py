from django.shortcuts import render
from .models import Book, Details
from django.http import Http404

# get books and render them to index.html
def index(request):
  booklist = Book.objects.order_by('book_name')[:50]
  context = {'booklist': booklist}
  return render(request, 'demoapp/index.html', context)

# book details with try except
def details(request, book_id):
  try:
    book = Book.objects.get(pk=book_id)
  except Book.DoesNotExist:
    raise Http404('Unexpected error')
  return render(request, 'demoapp/details.html', { 'book': book })