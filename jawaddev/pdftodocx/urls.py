from django.urls import path
from . import views

app_name = 'pdftodocx'

urlpatterns = [
    path('',views.pdftodocx.as_view(),name='pdftodocxconverter'),
    path('download/<str:fileName>/',views.download_docx, name='downloadDocx')
]
