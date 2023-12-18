from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('index/',views.PostIndexView.as_view(), name='post_index'),
    path('post/search/',views.PostSearchView.as_view(), name='post_search'),
    path('contents/',views.PostContentView.as_view(),name='post_content'),
    path('post/add/', views.PostCreateView.as_view(), name='post_add'),
    path('post/<slug:slug>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/edit/<slug:slug>/', views.PostUpdateView.as_view(), name='post_edit'),
    path('post/remove/<slug:slug>/', views.PostDeleteView.as_view(), name='post_remove'),
]
