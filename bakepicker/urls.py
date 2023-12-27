from django.urls import path
from . import views

app_name = 'bakepicker'

urlpatterns = [
    path('',views.bake_picker_index,name='bake_picker_index'),
    path('cake-and-recipe/',views.cake_and_recipe,name='cake_and_recipe'),
]
