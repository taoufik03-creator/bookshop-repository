from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Book
from .forms import BookForm

class BookListView(ListView):
    queryset=Book.objects.all()
    template_name="books/books.html"

class BookDetailView(DetailView):
    queryset=Book.objects.all()
    template_name="books/book.html"

class BookCreateView(CreateView):
    queryset=Book.objects.all()
    template_name="books/add_book.html"
    form_class=BookForm

class BookUpdateView(UpdateView):
    queryset=Book.objects.all()
    template_name="books/update_book.html"
    form_class=BookForm