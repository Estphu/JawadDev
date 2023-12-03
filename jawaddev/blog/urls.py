from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('index/',views.PostIndexView.as_view(), name='post_index'),
    path('post/search/',views.PostSearchView.as_view(), name='post_search'),
    path('post/<slug:slug>/', views.PostDetailView.as_view(), name='post_detail')
]
