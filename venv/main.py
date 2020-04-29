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

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


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
def DateFromText(text):
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
        return datetime.date(month=month, day=day, year=year)





class mainApp(Tk):
    def __init__(self):
        Tk.__init__(self)

        self._frame = None
        self.switch_frame(StartPage)
    def switch_frame(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

class StartPage(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        label = Label(self, text="Manage Your Tasks using Speech")
        label.pack()
        taskButton = Button(self, text="Task", fg="yellow", bg="red", font=("arial", 16, "bold"),
                                 command=lambda: master.switch_frame(TaskPage))
        taskButton.pack()
        todoButton = Button(self, text="To Do", fg="yellow", bg="red", font=("arial", 16, "bold"),
                                 command=lambda: master.switch_frame(ToDoPage))
        todoButton.pack()
        notesButton = Button(self, text="Notes", fg="yellow", bg="red", font=("arial", 16, "bold"),
                                 command=lambda: master.switch_frame(NotesPage))
        notesButton.pack()




class TaskPage(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        label1 = Label(self, text="Task Schedule:")
        label1.pack()
        label2 = Label(self, text="Add task using text or voice")
        label2.pack()

        self.task = StringVar()
        frametask = Frame(self)
        frametask.pack(fill=X)
        labeltask = Label(frametask, text="Task:", width=6)
        labeltask.pack(side=LEFT, padx=5, pady=5)
        entrytask = Entry(frametask,textvariable=self.task)
        entrytask.pack(side=LEFT,padx=5)
        speechtask = Button(frametask,text="Speak",command=lambda: self.get_task())
        speechtask.pack(side=LEFT, padx=5, pady=5)

        self.date = StringVar()
        framedate = Frame(self)
        framedate.pack(fill=X)
        labeldate = Label(framedate, text="Date:", width=6)
        labeldate.pack(side=LEFT, padx=5, pady=5)
        entrydate = Entry(framedate,textvariable=self.date)
        entrydate.pack(side=LEFT, padx=5)
        speechdate = Button(framedate, text="Speak",command=lambda: self.get_date())
        speechdate.pack(side=LEFT, padx=5, pady=5)

        frametime = Frame(self)
        frametime.pack(fill=X)
        labeltime = Label(frametime, text="Time:", width=6)
        labeltime.pack(side=LEFT, padx=5, pady=5)
        entrytime = Entry(frametime)
        entrytime.pack(side=LEFT, padx=5, expand=True)
        speechtime = Button(frametime, text="Speak",command=lambda: self.get_time())
        speechtime.pack(side=LEFT, padx=5, pady=5)

        addtask=Button(self,text="Add Task")
        addtask.pack()
        todoButton = Button(self, text="To Do", fg="yellow", bg="red", font=("arial", 16, "bold"),
                                 command=lambda: master.switch_frame(ToDoPage))
        todoButton.pack()
        notesButton = Button(self, text="Notes", fg="yellow", bg="red", font=("arial", 16, "bold"),
                                  command=lambda: master.switch_frame(NotesPage))
        notesButton.pack()

    def get_task(self):
        text = get_audio()
        self.task.set(text)

    def get_date(self):
        text = get_audio()
        tdate=DateFromText(text)
        self.date.set(tdate)

    def get_time(self):
        text = get_audio()
        tdate=DateFromText(text)
        self.date.set(tdate)


class ToDoPage(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        label = Label(self, text="To Do page")
        label.pack()

        self.todo = StringVar()
        frametodo1 = Frame(self)
        frametodo1.pack(fill=X)
        entrytodo = Entry(frametodo1,textvariable=self.todo)
        entrytodo.pack(side=LEFT,padx=5)
        speechtodo = Button(frametodo1, text="Speak",command=lambda: self.get_todo())
        speechtodo.pack(side=LEFT, padx=5, pady=5)
        addtodo = Button(self, text="Add to To-Do List")
        addtodo.pack()

        taskButton = Button(self, text="Task", fg="yellow", bg="red", font=("arial", 16, "bold"),
                                 command=lambda: master.switch_frame(TaskPage))
        taskButton.pack()
        notesButton = Button(self, text="Notes", fg="yellow", bg="red", font=("arial", 16, "bold"),
                                  command=lambda: master.switch_frame(NotesPage))
        notesButton.pack()

    def get_todo(self):
        text = get_audio()
        self.todo.set(text)

class NotesPage(Frame):
    def __init__(self,master):
        Frame.__init__(self, master)
        label = Label(self, text="Notes Page")
        label.pack()

        self.note = StringVar()
        framenote1 = Frame(self)
        framenote1.pack(fill=X)
        entrynote = Entry(framenote1,textvariable=self.note)
        entrynote.pack(side=LEFT, padx=5)
        speechnote = Button(framenote1, text="Speak",command=lambda: self.get_note())
        speechnote.pack(side=LEFT, padx=5, pady=5)
        addnote = Button(self, text="Add to Notes")
        addnote.pack()

        taskButton = Button(self, text="Task", fg="yellow", bg="red", font=("arial", 16, "bold"),
                                 command=lambda: master.switch_frame(TaskPage))
        taskButton.pack()
        todoButton = Button(self, text="To Do", fg="yellow", bg="red", font=("arial", 16, "bold"),
                                 command=lambda: master.switch_frame(ToDoPage))
        todoButton.pack()

    def get_note(self):
        text = get_audio()
        self.note.set(text)

if __name__ == "__main__":
    root = mainApp()
    root.title("Task Manager")
    root.mainloop()