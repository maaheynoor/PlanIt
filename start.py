import speech_recognition as sr
from gtts import gTTS
import os
import time
import datetime
import playsound
import pyttsx3
import re
import psycopg2     #database
from tkinter import *
import pyaudio

#import out modules
from startPage import StartPage

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




if __name__ == "__main__":
    root = mainApp()
    root.title("Task Manager")
    root.geometry("300x375")
    root.configure(background="SkyBlue4")
    root.mainloop()
