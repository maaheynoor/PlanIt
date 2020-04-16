from tkinter import *
import speech_recognition as sr
from gtts import gTTS
import os
import time
import datetime
import playsound

"""
from gtts import gTTS
import os
mytext="Hello Programming in Python"
language='en'
output=gTTS(text=mytext,lang=language,slow=False)
output.save("output.mp3")
os.system("start output.mp3")
"""
def speak(text="hello"):
    tts = gTTS(text=text, lang='en')
    filename = 'voice.mp3'
    tts.save(filename)
    #os.system("start output.mp3")
    playsound.playsound(filename)
    return

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""
        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception: " + str(e))
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
    if month < today.month and month != -1:  # if the month mentioned is before the current month set the year to the next
        year = year + 1

        # This is slighlty different from the video but the correct version
    if month == -1 and day != -1:  # if we didn't find a month, but we have a day
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


window=Tk()
window.geometry("1000x500")
window.title("Task Manager")
fn=StringVar()
label1=Label(window,text="Schedule your tasks with voicetm",fg="blue",font=("arial",16,"bold")).pack()
#pack to place at center, place(x=,y=) or label1.pack(fill=BOTH,pady=,padx=) or grid(row=,column=)
#pack(..,expand=True) Full screen filled with label
button1=Button(window,text="Speak",fg="yellow",bg="red",relief=RIDGE,font=("arial",16,"bold"),command=lambda: get_audio()) #GROOVE,RIDGE,SUNKEN,RAISED
button1.place(x=50,y=50)

entry1=Entry(window,width=25,font=("arial",16),textvar=fn)
entry1.place(x=50,y=100)

button2=Button(window,text="Convert to speech",fg="yellow",bg="red",relief=RIDGE,font=("arial",16,"bold"),command=lambda: speak("welcome back")) #GROOVE,RIDGE,SUNKEN,RAISED
button2.place(x=400,y=100)
window.mainloop()