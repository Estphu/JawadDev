from django import forms
from .models import Book, BookKeyPoint

class BookForm(forms.ModelForm):
    
    class Meta:
        model = Book
        fields = "__all__"

class BookKeyPointForm(forms.ModelForm):
    
    class Meta:
        model = BookKeyPoint
        fields = "__all__"        
