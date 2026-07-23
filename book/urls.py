from django.urls import path
from . import views

urlpatterns=[
    path("", views.BookListView.as_view(), name="book-list"),
    path("<uuid:pk>/", views.BookDetailView.as_view(), name="book-details"),
    path("add_book/", views.BookCreateView.as_view(), name="book-create"),
    path("<uuid:pk>/update/", views.BookUpdateView.as_view(), name="book-update"),
]