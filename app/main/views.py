from django.views.generic import View
from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
import speech_recognition as sr
from gtts import gTTS
import playsound
import time
import os

class SpeekView(View):
    def get(self, request, *args, **kwargs):

        text = 'Hello Ephrasia'

        tts = gTTS(text=text, lang='en')
        filename = 'voice.mp3'
        file_location = 'voice/'+filename
        tts.save(file_location)
        playsound.playsound(file_location)

        return HttpResponse('here please')

class GetAudioView(View):
    def speek(self, text, name):
        tts = gTTS(text=text, lang='en')
        file_location = 'voice/'+name
        tts.save(file_location)
        playsound.playsound(file_location)

    def get(self, request, *args, **kwargs):

        # NOTIFY USER TO SPEECH
        new_name = 'voice_'+str(time.time()).replace('.', '')+'.mp3'
        self.speek('Please Speek', new_name)

        r = sr.Recognizer()

        with sr.Microphone() as source:
            audio = r.listen(source)

            said = ''

            try:
                said = r.recognize_google(audio)
                print(said)
                return HttpResponse(said)
            except Exception as e:
                print('error', e)
                return HttpResponse(e)

class HomeView(View):
    template_name = 'main/home.html'
    def get(self, request, *args, **kwargs):
        key = self.request.GET.get('key', '')

        if key:
            voice = 'voice/pre/' + key + '.mpeg'
            playsound.playsound(voice)

        context = {}
        context['title'] = 'Home'
        context['buttons'] = range(1, 7)


        return render(request, self.template_name, context)
