from tkinter import *
from datetime import datetime
# import our class and functions

from assistantSpeak import assistant_speaks
from getAudio import get_audio
from getDateTime import *


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
        self.task = StringVar()
        self.date = StringVar()
        self.time = StringVar()
        self.taskFrame = Frame(self, width=300, height=100)
        self.taskFrame.pack(fill=BOTH, expand=TRUE, ipadx=10, pady=20)
        self.labelTask = Label(self.taskFrame, text='Task')
        self.labelTask.grid(row=0, column=0)
        self.inputTask = Entry(self.taskFrame,textvariable=self.task)
        self.inputTask.grid(row=0, column=1)
        self.labelDate = Label(self.taskFrame, text='Date')
        self.labelDate.grid(row=1, column=0)
        self.inputDate = Entry(self.taskFrame,textvariable=self.date)
        self.inputDate.grid(row=1, column=1)
        self.labelTime = Label(self.taskFrame, text='Time')
        self.labelTime.grid(row=2, column=0)
        self.inputTime = Entry(self.taskFrame,textvariable=self.time)
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
        assistant_speaks("Please specify the task to be performed")
        text = get_audio()
        self.task.set(text)
        assistant_speaks("Please specify the day")
        text = get_audio()
        tdate = DateFromText(text)  # get time from date
        self.date.set(tdate)
        assistant_speaks("Please mention the time")
        text = get_audio()
        time = TimeFromText(text)  # get time from text
        self.time.set(time)


    def actionAddTask(self):
        try:
            connection = psycopg2.connect(user="usertm",
                                          password="password",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="TaskManager")
            cursor = connection.cursor()
            task=self.inputTask.get()
            print(task)
            date = self.inputDate.get()
            print(date)
            time = self.inputTime.get()
            print(time)
            str = "INSERT INTO task(task,date,time) VALUES ('" + task + "','" + date + "','"+time+"');"
            cursor.execute(str)
            connection.commit()
            assistant_speaks("Task added successfully")
        except (Exception, psycopg2.DatabaseError) as error:
            connection.rollback()
            print("Error while using PostgreSQL table", error)
        finally:
            # closing database connection.
            if (connection):
                cursor.close()
                connection.close()

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


# Display task page
class DisplayTaskPage(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.back = Button(self, text="Back",
                           fg="white", bg="DeepPink2",
                           command=lambda: master.switch_frame(SchedulePage))
        self.back.grid(row=0, column=0,columnspan=4)
        self.display = Label(self, text="Display Tasks for which of the following:")
        self.display.grid(row=1, column=0,columnspan=4)
        self.radiovar = StringVar()
        # Option for specific day, btw two days, upcoming tasks or all task in the db
        self.R1 = Radiobutton(self, text="Specific Day",variable=self.radiovar, value="Specific Day", tristatevalue="x",
                              command=self.displayTask)
        self.R1.grid(row=2, column=0,columnspan=2)
        self.R2 = Radiobutton(self, text="Between two days", variable=self.radiovar, value="Between two days", tristatevalue="x",
                              command=self.displayTask)
        self.R2.grid(row=2, column=2,columnspan=2)
        self.R3 = Radiobutton(self, text="All Upcoming", variable=self.radiovar, value="All Upcoming", tristatevalue="x",
                              command=self.displayTask)
        self.R3.grid(row=3, column=0,columnspan=2)
        self.R4 = Radiobutton(self, text="All", variable=self.radiovar, value="All",
                              tristatevalue="x",
                              command=self.displayTask)
        self.R4.grid(row=3, column=2,columnspan=2)

        self.displayTask = Label(self)
        self.displayTask.grid(row=4,column=0,columnspan=4)

    def displayTask(self):
        selection = self.radiovar.get()
        input = False
        # For specific Day only one speech input is taken
        if selection == "Specific Day":
            assistant_speaks("Please mention the day")
            date=get_audio()
            date = DateFromText(date)
            if date==None:
                input=False
            else:
                input= True
        # Two days taken as input (start and end date)
        elif selection=="Between two days":
            assistant_speaks("Please mention the start date")
            sdate = get_audio()
            sdate=DateFromText(sdate)
            assistant_speaks("Please mention the end date")
            edate = get_audio()
            edate = DateFromText(edate)
            if sdate==None or edate==None:
                input=False
            else:
                input= True
        # No speech input for all upcoming or all tasks
        elif selection=="All Upcoming":
            today = datetime.date.today()
            input=True
        elif selection=="All":
            input=True

        # If speech input is identified and there are dates/days present in them
        if input==True:

            try:
                connection = psycopg2.connect(user="usertm",
                                              password="password",
                                              host="127.0.0.1",
                                              port="5432",
                                              database="TaskManager")
                cursor = connection.cursor()
                if selection == "Specific Day":
                    date = date.strftime("%Y-%m-%d")
                    print("Date:", date)
                    query = "SELECT * FROM task WHERE date='"+date+"' ORDER BY time;"
                    selection= selection+" : "+date
                elif selection=="Between two days":
                    sdate = sdate.strftime("%Y-%m-%d")
                    edate = edate.strftime("%Y-%m-%d")
                    print("Start Date:",sdate," End date:",edate)
                    query = "SELECT * FROM task WHERE date>='" + sdate + "' AND date<='"+edate+"' ORDER BY date,time;"
                    selection = " Between " + sdate+" and "+edate
                elif selection=="All Upcoming":
                    today = today.strftime("%Y-%m-%d")
                    query = "SELECT * FROM task WHERE date>='" + today + "' ORDER BY date,time;"
                    selection = "All Upcoming Tasks"
                elif selection == "All":
                    query = "SELECT * FROM task ORDER BY date,time;"
                    selection="All Tasks"
                cursor.execute(query)
                self.displayTask.config(text=selection)
                tasks=cursor.fetchall()
                # the data from db is display in grid with row>=5
                # First erase previous data
                for label in self.grid_slaves():
                    if int(label.grid_info()["row"]) >= 5:
                        label.grid_forget()
                index=5
                if len(tasks)>0:
                    stringtask="Task-Id\t\tTask\t\tDate\t\tTime\n"
                    Label(self, text="Task").grid(row=index, column=0)
                    Label(self, text="Date").grid(row=index, column=1)
                    Label(self, text="Time").grid(row=index, column=2)

                    # each task is displayed in a row and a delete button is associated with it
                    for task in tasks:
                        index = index + 1
                        Label(self, text=task[1]).grid(row=index, column=0)
                        Label(self, text=str(task[2])).grid(row=index, column=1)
                        Label(self, text=str(task[3])).grid(row=index , column=2)
                        Button(self, text="Delete",command=lambda id=task[0],row=index: self.deleteTask(id,row)).grid(row=index, column=3)
                        stringtask +=str(task[0])+"\t\t"+task[1]+"\t\t"+str(task[2])+"\t\t"+str(task[3])+"\n"
                    print(stringtask)
                    assistant_speaks("The Schedule is displayed")
                else:
                    assistant_speaks("There are no tasks")
                connection.commit()
            except (Exception, psycopg2.DatabaseError) as error:
                connection.rollback()
                print("Error while using PostgreSQL table", error)
            finally:
                # closing database connection.
                if (connection):
                    cursor.close()
                    connection.close()
        # If no day is recognized or speech is not identified then user can try again
        else:
            assistant_speaks("Please repeat the process. Couldn't identify your audio or date mentioned")


    def deleteTask(self,id,row):
        try:
            connection = psycopg2.connect(user="usertm",
                                          password="password",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="TaskManager")
            cursor = connection.cursor()
            query="DELETE FROM task WHERE task_id="+str(id)+";"
            cursor.execute(query)
            for label in self.grid_slaves():
                if int(label.grid_info()["row"])==row:
                    label.grid_forget()
            assistant_speaks("Deletion Successful")
            connection.commit()
        except (Exception , psycopg2.DatabaseError) as error:
            connection.rollback()
            print("Error while using PostgreSQL table", error)
        finally:
        # closing database connection.
            if (connection):
                cursor.close()
                connection.close()

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
