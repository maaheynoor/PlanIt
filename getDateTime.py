import speech_recognition as sr
from gtts import gTTS
import os
import time
import datetime
import playsound
import pyttsx3
import re
import psycopg2     #database
from tkinter import *       #GUI
#get date from text
MONTHS = ["january", "february", "march", "april", "may", "june","july", "august", "september","october", "november", "december"]
DAYS = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
DAY_EXTENTIONS = ["rd", "th", "st", "nd"]
def DateFromText(text):
    if text is not None:
        text = text.lower()
        today = datetime.date.today()
        if text.count("today") > 0:
            return today
        day = -1
        day_of_week = -1
        month = -1
        year = today.year
        if month < today.month and month != -1:  # if the month mentioned is before the current month set the year to the next
            year = year + 1

        for word in text.split():
            if word in MONTHS:
                month = MONTHS.index(word) + 1
            elif word in DAYS:
                day_of_week = DAYS.index(word)
            elif word.isdigit():
                if int(word)<=31:
                    day = int(word)
                if int(word)>=1000:
                    year=int(word)
            else:
                for ext in DAY_EXTENTIONS:
                    found = word.find(ext)
                    if found > 0:
                        try:
                            day = int(word[:found])
                        except:
                            pass


            # This is slighlty different from the video but the correct version
        if month == -1 and day != -1:  # if we didn't find a month, but we have a day
            if day < today.day:
                month = today.month + 1
            else:
                month = today.month

            # if we only found a day of the week
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
            try:
                return datetime.date(month=month, day=day, year=year)
            except:
                return None


PM=['pm','p.m.','afternoon','evening']
AM=['am','a.m.','morning']
def TimeFromText(text):
    if text is not None:
        text = text.lower()
        hour=-1
        minute=0
        second=0
        countnumber=0
        for word in re.split(' |:',text):
            if word.isdigit():
                if countnumber==0:
                    hour = int(word)
                    countnumber+=1
                elif countnumber==1:
                    minute = int(word)
        foundpm=[i for i in PM if(i in text.split())]
        foundam=[i for i in AM if(i in text.split())]
        if bool(foundpm) and hour>=1 and hour<=11:
            hour+=12
        if bool(foundam) and hour==12:
            hour-=12
        if hour!=-1:
            try:
                return datetime.time(hour=hour,minute=minute,second=second)
            except:
                return None
        else:
            return None

