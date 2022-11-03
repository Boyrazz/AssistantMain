import time

import pywhatkit

import webbrowser

import speech_recognition as sr

import pyautogui

import os

import getpass

import wikipedia

from playsound import playsound

from gtts import gTTS

from datetime import date, datetime

import random

from ctypes import cast,POINTER

from comtypes import CLSCTX_ALL

from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

from AppOpener import run


devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))


wikipedia.set_lang("tr")


r = sr.Recognizer()

acilis = random.randint(0,1)


def speak(string):
    tts = gTTS(text=string, lang="tr", slow=False)
    file = "answer.mp3"
    tts.save(file)
    # speeding()
    playsound(file)
    os.remove(file)
    # os.remove("speed.mp3")


def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            print(ask)
        r.adjust_for_ambient_noise(source,  duration=0.8)
        audio = r.listen(source)
        voice_data = ""
        try:
            voice_data = r.recognize_google(audio, language="TR-tr")
        except sr.UnknownValueError:
            print("Anlayamadım")
            pass
        except sr.RequestError:
            print("Sistem Hatası")
            pass
        print(voice_data)
        return voice_data


def respond(voice_data):
    if "merhaba" in voice_data:
        speak("Merhaba Efendim")

    if "internette ara" in voice_data:
        kelime = voice_data.split("internette ara", maxsplit=1)
        oge = kelime[1]
        url = "https://www.google.com.tr/search?q=" + oge
        webbrowser.get().open(url)

    if "kimdir" in voice_data:
        kelime = voice_data.split("kimdir", maxsplit =1)
        oge = kelime[0]
        url = "https://www.google.com.tr/search?q=" + oge
        webbrowser.get().open(url)
        result = wikipedia.summary(oge, sentences = 3)
        speak(result)

    if "nerede" in voice_data:
        kelime = voice_data.split("nerede", maxsplit=1)
        oge = kelime[0]
        url = "https://www.google.com.tr/maps/place/" + oge
        webbrowser.get().open(url)

    if "oynat" in voice_data:
        kelime = voice_data.split("oynat", maxsplit=1)
        oge = kelime[0]
        pywhatkit.playonyt(oge)

    if "ekran görüntüsü al" in voice_data:
        speak("Bi türlü yapamadık amık")
        
    if "hangi gündeyiz" in voice_data or "bugün günlerden ne" in voice_data:
        today = time.strftime("%A")
        today.capitalize()
        if today == "Monday":
            today = "Pazartesi"

        elif today == "Tuesday":
            today = "Salı"

        elif today == "Wednesday":
            today = "Çarşamba"

        elif today == "Thursday":
            today = "Perşembe"

        elif today == "Friday":
            today = "Cuma"
            webbrowser.get().open("https://www.youtube.com/shorts/NsM73MZtxGo")

        elif today == "Saturday":
            today = "Cumartesi"

        elif today == "Sunday":
            today = "Pazar"

        speak(today)

    if "saat kaç" in voice_data:
        selection = ["Saat şu an: ", "Hemen bakıyorum: "]
        clock = datetime.now().strftime("%H:%M")
        selection = random.choice(selection)
        speak(selection + clock)

    if "sesi ayarla" in voice_data:
        kelime = voice_data.split("sesi ayarla",maxsplit=1)
        oge = kelime[1]
        oge = oge.rstrip()
        print (oge)
        if oge == " bir":
            volume.SetMasterVolumeLevel(-50.0, None)
        if oge == ' 2':
            volume.SetMasterVolumeLevel(-20.0, None)
        if oge == ' 3':
            volume.SetMasterVolumeLevel(-10, None)
        if oge == ' 4':
            volume.SetMasterVolumeLevel(-0, None)

    if "bilgisayarı kapat" in voice_data:
        os.system("shutdown /s /t 1")
        
    if "pencereyi kapat" in voice_data:
        pyautogui.hotkey('altleft','f4')
        pyautogui.press('enter')

    if "programı kapat" in voice_data:
        playsound("shuttingdown.mp3")
        exit()

    if "prime video" in voice_data:
        kelime = voice_data.split("prime video",maxsplit=1)
        oge = kelime[1]
        run("prime video for windows")
        time.sleep(5)
        pyautogui.press(['tab', 'tab', 'tab', 'tab'])
        pyautogui.write(oge,)
        pyautogui.press("enter")
        time.sleep(3)
        pyautogui.click(x=497, y=581,button='left')
        time.sleep(3.5)
        pyautogui.click(x=1731, y=109,button='left')
    
    if "son bölümü aç" in voice_data:
        run("prime video for windows")
        time.sleep(8)
        pyautogui.click(x=607,y=487,button='left')
        time.sleep(3.5)
        play_button=pyautogui.locateOnScreen('Play_button.png')
        location = pyautogui.center(play_button)
        pyautogui.click(location)
        time.sleep(3.5)
        pyautogui.click(x=1731, y=109,button='left')
    




    if "youtube müzik" in voice_data:
        kelime = voice_data.split("youtube müzik",maxsplit = 1)
        oge = kelime[1]
        webbrowser.get().open(f"https://music.youtube.com/search?q={oge}")
        time.sleep(5)
        pyautogui.press(['tab', 'tab', 'tab', 'tab','tab','enter'])


    if "şarkıyı geri sar" in voice_data:
        pyautogui.press("h")

    if "önceki şarkıyı aç" in voice_data:
        pyautogui.press("k")

    if "sonraki şarkıya geç" in voice_data:
        pyautogui.press("j")

    if "şarkıyı ileri sar" in voice_data:
        pyautogui.press("l")

    if "şarkıyı durdur" in voice_data:
        pyautogui.press("enter")

    if "Whatsapp" in voice_data:
        run("Whatsapp")
        time.sleep(5)
        pyautogui.press("alt")

    if "wubalubadubdub" in voice_data:
        playsound("wubbalubba.mp3")
        pywhatkit.playonyt("https://www.youtube.com/watch?v=L5ozF8HuT4k")



def test(wake):
    if"ceviz" in wake:
        playsound("DING.mp3")
        wake = record_audio()
        if wake != '':
            voice_data = wake.lower()
            respond(voice_data)

if acilis == 1:
    playsound("activate_sound.mp3")
else:
    playsound("came_back_sound.mp3")

while True:
    wake = record_audio()
    if wake != '':
        wake = wake.lower()
        test(wake)

