import speech_recognition as sr
from gtts import gTTS
import os
import time
import datetime
import playsound
import pyttsx3          #there were errors while installing but got automatically solved after few days
import re

def speak(text):
    engine = pyttsx3.init()
    #errors while using engine = pyttsx3.init() solved using dummy as parameter but doesnt produce any sound
    #but now working without dummy
    engine.say(text)
    engine.runAndWait()


"""
this speech function can be used only one time. When you call the same function second time it throws error
with open(str(savefile), 'wb') as f:
PermissionError: [Errno 13] Permission denied: 'voice.mp3'
def speak2(text):
    tts = gTTS(text=text, lang='en')
    filename = 'voice.mp3'
    tts.save(filename)
    playsound.playsound(filename)
    return
"""

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""
        try:
            said = r.recognize_google(audio)
            print("You:",said)
        except Exception as e:
            print("Exception: Something went wrong" + str(e))
            speak("Something went wrong")
    return said

#get date from text
MONTHS = ["january", "february", "march", "april", "may", "june","july", "august", "september","october", "november", "december"]
DAYS = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
DAY_EXTENTIONS = ["rd", "th", "st", "nd"]
def get_date(text):
    text = text.lower()
    today = datetime.date.today()
    if text.count("today") > 0:
        return today
    day = -1
    day_of_week = -1
    month = -1
    year = today.year

    for word in text.split():
        if word in MONTHS:
            month = MONTHS.index(word) + 1
        elif word in DAYS:
            day_of_week = DAYS.index(word)
        elif word.isdigit():
            day = int(word)
        else:
            for ext in DAY_EXTENTIONS:
                found = word.find(ext)
                if found > 0:
                    try:
                        day = int(word[:found])
                    except:
                        pass
    if month < today.month and month != -1:
        year = year + 1

    if month == -1 and day != -1:
        if day < today.day:
            month = today.month + 1
        else:
            month = today.month

        # if we only found a dta of the week
    if month == -1 and day == -1 and day_of_week != -1:
        current_day_of_week = today.weekday()
        dif = day_of_week - current_day_of_week
        if dif < 0:
            dif += 7
        if text.count("next") >= 1:
            dif += 7
        return today + datetime.timedelta(dif)
    if month == -1 or day == -1:
        return None
    if day != -1:
        return datetime.date(month=month, day=day, year=year)

#add task to the notes
# format for entering into note - Date Time Description of work
addtask = ["have to", "have a", "is a","need to"]
checktask = ["what do i have", "do i have ", "am i busy"]
to_exit=["bye","exit"]

def add_task(text):
    date=get_date(text)
    work=re.split(r'have to|have a|is a|need to',text)
    file=open("note.txt","a")
    file.write(str(date)+"\t"+work[1]+"\n")


def check_task(text):
    speak("Checking..")
    count=0
    date = get_date(text)
    if date:
        file = open("note.txt")
        while True:
            line = file.readline()
            if not line:
                break
            if str(date) in line:
                print(line)
                count+=1
        if count==0:
            speak("You have no task scheduled on the desired day")
        else:
            speak("Yes you have some work for the given day")
    else:
        speak("Please Try Again")


speak("Welcome to Task Manager")
speak("How can I help you?")
exit=False
while not exit:
    user_says=get_audio()
    if user_says:
        for phrase in checktask:
            if phrase in user_says.lower():
                check_task(user_says)
                break
        for phrase in addtask:
            if phrase in user_says.lower():
                add_task(user_says)
                break
        for phrase in to_exit:
            if phrase in user_says.lower():
                speak("Thank You! Have a Good Day")
                exit=True
                break
    if not exit:
        speak("Do you need any other help in managing your tasks?")













