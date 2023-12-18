from django.urls import path
from . import views

app_name = 'readinglist'

urlpatterns = [
    path('',views.BookListView.as_view(),name='book_list'),
    path('book/add/',views.BookCreateView.as_view(),name='book_add'),
    path('book/edit/<int:pk>/',views.BookUpdateView.as_view(),name='book_edit'),
    path('book/remove/<int:pk>/',views.BookDeleteView.as_view(),name='book_remove'),
    path('book-key-point/<int:pk>/add/',views.BookKeyPointCreateView.as_view(),name='book_kp_add'),
    path('book-key-point/edit/<int:pk>/',views.BookKeyPointUpdateView.as_view(),name='book_kp_edit'),
    path('book-key-point/remove/<int:pk>',views.BookKeyPointDeleteView.as_view(),name='book_kp_remove'),
]
