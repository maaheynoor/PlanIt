from tkinter import *

# import our class and functions

from assistantSpeak import assistant_speaks
from getAudio import get_audio


class StartPage(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master

        # schedule and help frame
        self.topButtonFrame = Frame(self, width=300, height=50)
        self.topButtonFrame.pack(fill=BOTH, expand=TRUE, ipadx=10, pady=20)
        schedule = Button(self.topButtonFrame, text="schedule",
                          fg="white", bg="DeepPink2",
                          command=lambda: self.master.switch_frame(SchedulePage))
        schedule.pack(side=LEFT)
        help = Button(self.topButtonFrame, text="help",
                      fg="white", bg="DeepPink2",
                      command=lambda: self.master.switch_frame(HelpPage))
        help.pack(side=RIGHT)

        # task manager
        self.taskFrame = Frame(self, width=300, height=100)
        self.taskFrame.pack(fill=BOTH, expand=TRUE, ipadx=10, pady=20)
        self.labelTask = Label(self.taskFrame, text='Task')
        self.labelTask.grid(row=0, column=0)
        self.inputTask = Entry(self.taskFrame)
        self.inputTask.grid(row=0, column=1)
        self.labelDate = Label(self.taskFrame, text='Date')
        self.labelDate.grid(row=1, column=0)
        self.inputDate = Entry(self.taskFrame)
        self.inputDate.grid(row=1, column=1)
        self.labelTime = Label(self.taskFrame, text='Time')
        self.labelTime.grid(row=2, column=0)
        self.inputTime = Entry(self.taskFrame)
        self.inputTime.grid(row=2, column=1)
        self.mikeTask = Button(self.taskFrame, text="Speak", fg="white", bg="DeepPink2",
                               command=lambda: self.actionSpeakTask())
        self.mikeTask.grid(row=3, column=0)
        self.addTask = Button(self.taskFrame, text="Add", fg="white", bg="DeepPink2",
                              command=lambda: self.actionAddTask())
        self.addTask.grid(row=3, column=1)

        # todomanager
        self.todoFrame = Frame(self, width=300, height=100)
        self.todoFrame.pack(fill=BOTH, expand=TRUE, ipadx=10, pady=20)
        self.labelTodo = Label(self.todoFrame, text='Todo')
        self.labelTodo.grid(row=0, column=0)
        self.inputTodo = Entry(self.todoFrame)
        self.inputTodo.grid(row=0, column=1)
        self.mikeTodo = Button(self.todoFrame, text="Speak", fg="white", bg="DeepPink2",
                               command=lambda: self.actionSpeakTodo())
        self.mikeTodo.grid(row=1, column=0)
        self.addTodo = Button(self.todoFrame, text="Add", fg="white", bg="DeepPink2",
                              command=lambda: self.actionAddTodo())
        self.addTodo.grid(row=1, column=1)

        # note manager
        self.noteFrame = Frame(self, width=300, height=100)
        self.noteFrame.pack(fill=BOTH, expand=TRUE, ipadx=10, pady=20)
        self.labelNote = Label(self.noteFrame, text='Note')
        self.labelNote.grid(row=0, column=0)
        self.inputNote = Entry(self.noteFrame)
        self.inputNote.grid(row=0, column=1)
        self.mikeNote = Button(self.noteFrame, text="Speak", fg="white", bg="DeepPink2",
                               command=lambda: self.actionSpeakNote())
        self.mikeNote.grid(row=1, column=0)
        self.addNote = Button(self.noteFrame, text="Add", fg="white", bg="DeepPink2",
                              command=lambda: self.actionAddNote())
        self.addNote.grid(row=1, column=1)

    def actionSpeakTask(self):
        assistant_speaks('How can I help you ?')
        self.inputTask.delete(0, END)
        self.inputDate.delete(0, END)
        self.inputTime.delete(0, END)
        voice = get_audio()
        voice = voice.lower()
        print(voice)

    def actionAddTask(self):
        pass

    def actionSpeakTodo(self):
        assistant_speaks('How can I help you ?')
        self.inputTodo.delete(0, END)
        voice = get_audio()
        voice = voice.lower()
        print(voice)

    def actionAddTodo(self):
        pass

    def actionSpeakNote(self):
        assistant_speaks('How can I help you ?')
        self.inputTodo.delete(0, END)
        voice = get_audio()
        voice = voice.lower()
        print(voice)

    def actionAddNote(self):
        pass


class SchedulePage(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.back = Button(self, text="Back",
                           fg="white", bg="DeepPink2",
                           command=lambda: master.switch_frame(StartPage))
        self.back.grid(row=0, column=0)
        self.displayTaskButton = Button(self, text="Display Tasks",
                                        fg="white", bg="DeepPink2",
                                        command=lambda: master.switch_frame(DisplayTaskPage))
        self.displayTaskButton.grid(row=1, column=0)
        self.displayNoteButton = Button(self, text="Display Notes",
                                        fg="white", bg="DeepPink2",
                                        command=lambda: master.switch_frame(DisplayNotePage))
        self.displayNoteButton.grid(row=2, column=0)


class DisplayTaskPage(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.back = Button(self, text="Back",
                           fg="white", bg="DeepPink2",
                           command=lambda: master.switch_frame(SchedulePage))
        self.back.grid(row=0, column=0)


class DisplayNotePage(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.back = Button(self, text="Back",
                           fg="white", bg="DeepPink2",
                           command=lambda: master.switch_frame(SchedulePage))
        self.back.grid(row=0, column=0)


class HelpPage(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.back = Button(self, text="Back",
                           fg="white", bg="DeepPink2",
                           command=lambda: master.switch_frame(SchedulePage))
        self.back.grid(row=0, column=0)
