from django.urls import path
from . import views

app_name = 'readinglist'

urlpatterns = [
    path('',views.BookListView.as_view(),name='book_list'),
    path('add/',views.BookCreateView.as_view(),name='book_add'),
    path('edit/<int:pk>/',views.BookUpdateView.as_view(),name='book_edit'),
    path('remove/<int:pk>/',views.BookDeleteView.as_view(),name='book_remove'),
    path('book-key-point/add/',views.BookKeyPointCreateView.as_view(),name='book_kp_add'),
]
