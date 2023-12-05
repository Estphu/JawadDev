from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Book, BookKeyPoint
from .forms import BookForm, BookKeyPointForm

# Create your views here.
class BookListView(ListView):
    model = Book
    template_name = 'readinglist/book_list.html'
    context_object_name = 'books'

    def get_queryset(self):
        return Book.objects.filter(user=3)
    
class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    form_class = BookForm
    success_url = reverse_lazy('readinglist:book_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(BookCreateView, self).form_valid(form)
    
class BookUpdateView(LoginRequiredMixin, UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'readinglist/book_form.html'
    success_url = reverse_lazy('readinglist:book_list')

class BookDeleteView(LoginRequiredMixin, DeleteView):
    model = Book
    template_name = 'readinglist/book_confirm_delete.html'
    success_url = reverse_lazy('readinglist:book_list')

class BookKeyPointCreateView(CreateView, LoginRequiredMixin):
    login_url = '/'
    success_url = reverse_lazy('readinglist:book_list')
    form_class = BookKeyPointForm
    model = BookKeyPoint
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(BookKeyPointCreateView, self).form_valid(form)    