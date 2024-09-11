from django.urls import path, include
from main.views import show_main, create_mood_entry

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('', include('main.urls')),
    path('create-mood-entry', create_mood_entry, name='create_mood_entry'),
]