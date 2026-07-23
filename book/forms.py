from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model=Book
        exclude=["id"]
        widgets={
            "release_date":forms.DateInput(attrs={
                "type":"date"
            })
        }