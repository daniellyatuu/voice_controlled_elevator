from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('speek/', views.SpeekView.as_view(), name='speek_view'),
    path('get-audio/', views.GetAudioView.as_view(), name='get_audio_view'),
    path('check-port/', views.CheckSerialPort.as_view(), name='check_port'),
    path('control-port/', views.ControlSerialPort.as_view(), name='control_port'),
    path('home/', views.HomeView.as_view(), name='home'),
]
