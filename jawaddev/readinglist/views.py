from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Book, BookKeyPoint
from .forms import BookForm, BookKeyPointForm

# Create your views here.
class BookListView(ListView):
    template_name = 'readinglist/book_list.html'
    context_object_name = 'books'
    model = Book

    def get_queryset(self):
        return Book.objects.filter(user=3)
    
class BookCreateView(LoginRequiredMixin, CreateView):
    success_url = reverse_lazy('readinglist:book_list')
    model = Book
    fields = ['thumbnail_url', 'link_url', 'title', 'tag', 'author', 'desc', 'extra', 'is_published']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def get_queryset(self):
        return Book.objects.filter(user=self.request.user)
    
class BookUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'readinglist/book_form.html'
    success_url = reverse_lazy('readinglist:book_list')
    form_class = BookForm
    model = Book

    def get_queryset(self):
        return Book.objects.filter(user=self.request.user)

class BookDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'readinglist/book_confirm_delete.html'
    success_url = reverse_lazy('readinglist:book_list')
    model = Book

class BookKeyPointCreateView(LoginRequiredMixin, CreateView):
    login_url = '/'
    success_url = reverse_lazy('readinglist:book_list')
    model = BookKeyPoint
    fields = ['book','point']
    
    def get_queryset(self):
        return Book.objects.filter(user=self.request.user)

class BookKeyPointUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'readinglist/bookkeypoint_form.html'
    success_url = reverse_lazy('readinglist:book_list')
    form_class = BookKeyPointForm
    model = BookKeyPoint

class BookKeyPointDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'readinglist/bookkeypoint_confirm_delete.html'
    success_url = reverse_lazy('readinglist:book_list')
    model = BookKeyPoint