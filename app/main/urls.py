from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('speek/', views.SpeekView.as_view(), name='speek_view'),
    path('get-audio/', views.GetAudioView.as_view(), name='get_audio_view'),
    path('get-audio/', views.GetAudioView.as_view(), name='get_audio_view'),
    path('home/', views.HomeView.as_view(), name='home'),
]
