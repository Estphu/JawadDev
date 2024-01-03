from django.urls import path
from . import views

app_name = 'scraping'

urlpatterns = [
    path('scraping-options/',views.scraping_options,name='options'),
    path('quaid-e-azam-speech/',views.get_quaid_speech,name='quaid-speech'),
    path('abraham-lincoln-speech/',views.get_abraham_speech,name='abraham-speech')
]
