from django.urls import path
from . import views

app_name = "portfolio"

urlpatterns = [
    path('',views.ProjectListView.as_view(),name='project_list'),
    path('project/add/',views.ProjectCreatView.as_view(),name='project_add'),
    path('project/edit/<int:pk>/',views.ProjectUpdateView.as_view(),name='project_edit'),
    path('project/remove/<int:pk>/',views.ProjectDeleteView.as_view(),name='project_remove'),
    path('review/<slug:slug>/',views.ProjectReview.as_view(),name='review_detail')
]
