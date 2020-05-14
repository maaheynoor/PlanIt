from tkinter import *
from datetime import datetime

# import our class and functions
from assistantSpeak import assistant_speaks
from getAudio import get_audio
from getDateTime import *
from getWigetList import all_children
from scroll import ScrollFrame
from todoDB import todoDbAction


class StartPage(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master

        # speak icon image
        self.mikeTodo = PhotoImage(file='images\mike5.png')
        self.speakicon = self.mikeTodo.subsample(25, 20)

        # task manager
        self.task = StringVar()
        self.date = StringVar()
        self.time = StringVar()
        self.taskFrame = Frame(self, width=300, height=100, bd=2, relief=RAISED)
        self.taskFrame.grid(row=0, column=0, padx=2, pady=5, sticky='news')
        self.taskheading = Label(self.taskFrame, text='Task', font=('Verdana', 12, 'bold'), bg="peachpuff",
                                 fg="deeppink4")
        self.taskheading.grid(row=0, column=0, columnspan=3, pady=3)
        self.labelTask = Label(self.taskFrame, text='Task', font=('calibri', 10), fg='black')
        self.labelTask.grid(row=1, column=0, pady=3)
        self.inputTask = Entry(self.taskFrame, textvariable=self.task)
        self.inputTask.grid(row=1, column=1, pady=3)
        self.labelDate = Label(self.taskFrame, text='Date', font=('calibri', 10), fg='black')
        self.labelDate.grid(row=2, column=0, pady=3)
        self.inputDate = Entry(self.taskFrame, textvariable=self.date)
        self.inputDate.grid(row=2, column=1, pady=3)
        self.labelTime = Label(self.taskFrame, text='Time', font=('calibri', 10), fg='black')
        self.labelTime.grid(row=3, column=0, pady=3)
        self.inputTime = Entry(self.taskFrame, textvariable=self.time)
        self.inputTime.grid(row=3, column=1, pady=3)
        self.s = Button(self.taskFrame, image=self.speakicon, height=50, command=lambda: self.actionSpeakTask())
        self.s.image = self.speakicon
        self.s.grid(row=1, column=2, rowspan=4, padx=5, ipadx=3)

        self.addTask = Button(self.taskFrame, text="Add", fg="peachpuff", bg="hotpink4", font=('Verdana', 11),
                              command=lambda: self.actionAddTask())
        self.addTask.grid(row=6, column=0, columnspan=2, pady=3)

        # todomanager
        self.todoFrame = Frame(self, width=300, height=100, bd=2, relief=RAISED)
        self.todoFrame.grid(row=1, column=0, padx=2, pady=5, sticky='news')
        self.todoheading = Label(self.todoFrame, text='ToDo', font=('Verdana', 12, 'bold'), bg="peachpuff",
                                 fg="deeppink4")
        self.todoheading.grid(row=0, column=0, columnspan=3, pady=3)
        self.labelTodo = Label(self.todoFrame, text='Todo', font=('calibri', 10), fg='black')
        self.labelTodo.grid(row=1, column=0, pady=3)
        self.inputTodo = Entry(self.todoFrame)
        self.inputTodo.grid(row=1, column=1, pady=3)

        self.s = Button(self.todoFrame, image=self.speakicon, compound=LEFT,
                        command=lambda: self.actionSpeakTodo())
        self.s.image = self.speakicon
        self.s.grid(row=1, column=2, padx=5, ipadx=3)

        self.addTodo = Button(self.todoFrame, text="Create", fg="peachpuff", bg="hotpink4", font=('Verdana', 11),
                              command=lambda: self.actionAddTodo())
        self.addTodo.grid(row=3, column=0, columnspan=2, pady=3)
        self.todoFile = None

        # note manager
        self.title = StringVar()
        self.noteFrame = Frame(self, width=300, height=100, bd=2, relief=RAISED)
        self.noteFrame.grid(row=2, column=0, padx=2, pady=5, sticky='news')
        self.noteheading = Label(self.noteFrame, text='Note', font=('Verdana', 12, 'bold'), bg="peachpuff",
                                 fg="deeppink4")
        self.noteheading.grid(row=0, column=0, columnspan=3, pady=3)
        self.labelTitle = Label(self.noteFrame, text='Title', font=('calibri', 10), fg='black')
        self.labelTitle.grid(row=1, column=0, pady=3)
        self.inputTitle = Entry(self.noteFrame, textvariable=self.title)
        self.inputTitle.grid(row=1, column=1, pady=3)
        self.s = Button(self.noteFrame, image=self.speakicon, compound=LEFT,
                        command=lambda: self.actionSpeakNoteTitle())
        self.s.image = self.speakicon
        self.s.grid(row=1, column=2, padx=5, ipadx=3)
        self.labelNote = Label(self.noteFrame, text='Note', font=('calibri', 10), fg='black')
        self.labelNote.grid(row=2, column=0, pady=3)
        self.inputNote = Text(self.noteFrame, height=5, width=20)
        self.inputNote.grid(row=2, column=1, pady=3)
        self.s = Button(self.noteFrame, image=self.speakicon, compound=LEFT,
                        command=lambda: self.actionSpeakNote())
        self.s.image = self.speakicon
        self.s.grid(row=2, column=2, padx=5, ipadx=3)

        self.addNote = Button(self.noteFrame, text="Add", fg="peachpuff", bg="hotpink4", font=('Verdana', 11),
                              command=lambda: self.actionAddNote())
        self.addNote.grid(row=4, column=0, columnspan=2, pady=3)

        # schedule and help frame in the bottom
        """ master is frame containing contents
        master.master is canvas
        master.master.master is frame containing canvas used for switching between pages"""
        self.topButtonFrame = Frame(self, width=300, bd=2, relief=RAISED, height=100)
        self.topButtonFrame.grid(row=3, column=0, padx=2, pady=5)
        schedule = Button(self.topButtonFrame, text="Schedule",
                          fg="peachpuff", bg="hotpink4", font=('Verdana', 10, 'bold'),
                          command=lambda: self.master.master.master.switch_frame(SchedulePage))
        schedule.grid(row=0, column=0, padx=2, pady=2)
        help = Button(self.topButtonFrame, text="Help",
                      fg="peachpuff", bg="hotpink4", font=('Verdana', 10, 'bold'),
                      command=lambda: self.master.master.master.switch_frame(HelpPage))
        help.grid(row=0, column=1, padx=2, pady=2)

        # side display frame
        self.displayFrame = Frame(self, width=190, bd=5, relief=RAISED)
        self.displayFrame.grid(row=0, column=1, rowspan=4, padx=2, pady=5, sticky='news')
        self.scrollBar = ScrollFrame(self.displayFrame, 190, 425)
        self.scrollBar.pack(side="top", fill="both", expand=True)

    def actionSpeakTask(self):
        assistant_speaks('How can I help you ?')
        assistant_speaks("Please specify the task to be performed")
        text = get_audio()
        if text is not None:
            self.task.set(text)
        assistant_speaks("Please specify the day")
        text = get_audio()
        tdate = DateFromText(text)  # get time from date
        if tdate is not None:
            self.date.set(tdate)
        assistant_speaks("Please mention the time")
        text = get_audio()
        time = TimeFromText(text)  # get time from text
        if time is not None:
            self.time.set(time)

    def actionAddTask(self):
        try:
            connection = psycopg2.connect(user="usertm",
                                          password="password",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="TaskManager")
            cursor = connection.cursor()
            task = self.inputTask.get()
            print(task)
            date = self.inputDate.get()
            print(date)
            time = self.inputTime.get()
            print(time)
            if len(task)!=0 and len(date)!=0:
                if len(time)!=0:
                    str = "INSERT INTO task(task,date,time) VALUES ('" + task + "','" + date + "','" + time + "');"

                else:
                    str = "INSERT INTO task(task,date) VALUES ('" + task + "','" + date + "');"
                cursor.execute(str)
                connection.commit()
                assistant_speaks("Task added successfully")
                self.inputTask.delete(0, END)
                self.inputDate.delete(0, END)
                self.inputTime.delete(0, END)
            elif len(task)==0:
                assistant_speaks("Please enter task")
            elif len(date)==0:
                assistant_speaks("Please enter date")

        except (Exception, psycopg2.DatabaseError) as error:
            connection.rollback()
            print("Error while using PostgreSQL table", error)
        finally:
            # closing database connection.
            if (connection):
                cursor.close()
                connection.close()

    def displayTodoInSideFrame(self):
        widget_list = all_children(self.displayFrame)
        for item in widget_list:
            item.grid_forget()
        try:
            connection = psycopg2.connect(user="usertm",
                                          password="password",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="TaskManager")
            cursor = connection.cursor()
            if self.todoFile is None:
                str = 'select list_name from todo_list_name order by list_name'
                cursor.execute(str)
                rows = cursor.fetchall()
                i = 0
                for row in rows:
                    Label(self.scrollBar.viewPort, text=row[0], fg="hotpink4", borderwidth=2, width=14,
                          relief="ridge", font=('Verdana', 15)).grid(row=i, column=0)
                    i += 1
            else:
                str = "select todo_name,completed from todo_names where list_name = '%s' order by todo_name"
                args = self.todoFile
                cursor.execute(str % args)
                rows = cursor.fetchall()
                if len(rows) == 0:
                    todoDbAction('Create', None, self.todoFile)
                Label(self.scrollBar.viewPort, text=self.todoFile, fg="hotpink4", borderwidth=2, width=16,
                      relief="ridge", font=('Verdana', 15, 'bold')).grid(row=0, column=0)
                i = 1
                for row in rows:
                    if row[1]:
                        Label(self.scrollBar.viewPort, text=row[0], fg='pink', width=28, font=('Verdana', 10)).grid(
                            row=i, column=0)
                    else:
                        Label(self.scrollBar.viewPort, text=row[0], fg="hotpink4", width=28, font=('Verdana', 10)).grid(
                            row=i, column=0)
                    i += 1
        except (Exception, psycopg2.DatabaseError) as error:
            connection.rollback()
            print("Error while using PostgresSQL table", error)
        finally:
            # closing database connection.
            if connection:
                cursor.close()
                connection.close()

    def actionSpeakTodo(self):
        self.inputTodo.delete(0, END)
        assistant_speaks("How can I hep you ? ")
        voice = get_audio()
        if self.todoFile is None and voice is not None:
            if voice.startswith('create'):
                self.addTodo['text'] = "Create"
                self.inputTodo.insert(0, voice[7:])
            elif voice.startswith('open'):
                self.addTodo['text'] = "Open"
                self.inputTodo.insert(0, voice[5:])
            elif voice.startswith('display'):
                self.addTodo['text'] = "Display"
                self.inputTodo.insert(0, voice)
            elif voice.startswith('delete'):
                self.addTodo['text'] = "Delete"
                self.inputTodo.insert(0, voice[7:])
            else:
                assistant_speaks("Unknown command")
        elif voice is not None:
            if voice.startswith('add'):
                self.addTodo['text'] = "Add"
                self.inputTodo.insert(0, voice[4:])
            elif voice.startswith('check'):
                self.addTodo['text'] = "Check"
                self.inputTodo.insert(0, voice[6:])
            elif voice.startswith('delete'):
                self.addTodo['text'] = "Delete"
                self.inputTodo.insert(0, voice[7:])
            elif voice.startswith('uncheck'):
                self.addTodo['text'] = "Uncheck"
                self.inputTodo.insert(0, voice[8:])
            elif voice.startswith('clear'):
                self.addTodo['text'] = "Clear All"
                self.inputTodo.insert(0, voice)
            elif voice.startswith('exit'):
                self.addTodo['text'] = "Exit"
                self.inputTodo.insert(0, voice)
            else:
                assistant_speaks("Unknown command")

    def actionAddTodo(self):
        command = self.addTodo['text']
        work = self.inputTodo.get().strip()
        if self.todoFile is None and command != 'Display':
            if command == 'Open':
                self.addTodo['text'] = 'Add'
                self.todoFile = work
            else:
                todoDbAction(command, None, work)
                todoDbAction('Clear All', 'new', work)
                self.addTodo['text'] = 'Create'
        elif self.todoFile is not None:
            if command == 'Exit':
                self.todoFile = None
                self.addTodo['text'] = 'Create'
            else:
                todoDbAction(command, work, self.todoFile)
                self.addTodo['text'] = 'Add'
        else:
            self.addTodo['text'] = 'Create'
        self.displayTodoInSideFrame()
        self.inputTodo.delete(0, END)

    def displayNoteInSideFrame(self):
        pass

    def actionSpeakNoteTitle(self):
        self.inputTitle.delete(0, END)
        assistant_speaks("Please specify the title of note")
        text = get_audio()
        self.title.set(text)
        print(text)

    def actionSpeakNote(self):
        # self.inputNote.delete(0, END)
        assistant_speaks('Please specify the note to be added')
        voice = get_audio()
        self.inputNote.insert(END, voice)
        print(self.inputNote.get("1.0", END))

    def actionAddNote(self):
        try:
            connection = psycopg2.connect(user="usertm",
                                          password="password",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="TaskManager")
            cursor = connection.cursor()
            title = self.inputTitle.get()
            print(title)
            note = self.inputNote.get("1.0", END)
            print(note)
            now = datetime.datetime.now()
            date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
            print(date_time)
            if len(self.inputNote.get("1.0","end-1c"))!=0:
                str = "INSERT INTO note(note,title,date_created,date_modified) VALUES ('" + note + "','" + title + "','" + date_time + "','" + date_time + "');"
                cursor.execute(str)
                connection.commit()
                assistant_speaks("Note added successfully")
            else:
                assistant_speaks("Note cannot be empty")
            self.inputTitle.delete(0, END)
            self.inputNote.delete(1.0, END)
        except (Exception, psycopg2.DatabaseError) as error:
            connection.rollback()
            print("Error while using PostgreSQL table", error)
        finally:
            # closing database connection.
            if (connection):
                cursor.close()
                connection.close()


class SchedulePage(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        # buttons
        self.buttonsFrame = Frame(self)
        self.buttonsFrame.grid(row=0, column=0, padx=5, pady=3)
        self.displayTaskButton = Button(self.buttonsFrame, text="Display Tasks",
                                        fg="peachpuff", bg="hotpink4", font=('Verdana', 10, 'bold'),
                                        command=lambda: self.displayTaskAction())
        # command=lambda: master.master.master.switch_frame(DisplayTaskPage))
        self.displayTaskButton.grid(row=0, column=1, padx=3, pady=3)
        self.displayTodoButton = Button(self.buttonsFrame, text="Display ToDo",
                                        fg="peachpuff", bg="hotpink4", font=('Verdana', 10, 'bold'),
                                        command=lambda: self.displayTodoAction())
        # command=lambda: master.master.master.switch_frame(DisplayTodoPage))
        self.displayTodoButton.grid(row=0, column=2, padx=3, pady=3)
        self.displayNoteButton = Button(self.buttonsFrame, text="Display Notes",
                                        fg="peachpuff", bg="hotpink4", font=('Verdana', 10, 'bold'),
                                        command=lambda: self.displayNoteAction())
        # command=lambda: master.master.master.switch_frame(DisplayNotePage))
        self.displayNoteButton.grid(row=0, column=3, padx=3, pady=3)

        # display
        self.displayAll = Frame(self, width=450, height=425, bd=5, relief=RAISED)
        self.displayAll.grid(row=1, column=0, padx=5, pady=5, sticky='news')
        self.scrollFrame = ScrollFrame(self.displayAll, 425, 425)
        self.scrollFrame.pack(side="top", fill="both", expand=True)

        # init of display task
        self.initTask()

        # init of display to do
        self.initTodo()

        # init of display note
        self.initNote()

        # back
        self.back = Button(self, text="Back",
                           fg="peachpuff", bg="hotpink4", font=('Verdana', 10, 'bold'),
                           command=lambda: master.master.master.switch_frame(StartPage))
        self.back.grid(row=2, column=0, padx=5, pady=5)

    def initTask(self):
        self.display = Label(self.scrollFrame.viewPort, text="Display Tasks for which of the following:",
                             font=("calibri", 12, "bold"))
        self.font = ("calibri", "11")
        self.radiovar = StringVar()
        # Option for specific day, btw two days, upcoming tasks or all task in the db
        self.R1 = Radiobutton(self.scrollFrame.viewPort, text="Specific Day", variable=self.radiovar,
                              value="Specific Day",
                              tristatevalue="x",
                              font=self.font, command=lambda: self.displayTask())
        self.R2 = Radiobutton(self.scrollFrame.viewPort, text="Between two days", variable=self.radiovar,
                              value="Between two days",
                              tristatevalue="x",
                              font=self.font, command=lambda: self.displayTask())
        self.R3 = Radiobutton(self.scrollFrame.viewPort, text="All Upcoming", variable=self.radiovar,
                              value="All Upcoming",
                              tristatevalue="x",
                              font=self.font, command=lambda: self.displayTask())
        self.R4 = Radiobutton(self.scrollFrame.viewPort, text="All", variable=self.radiovar, value="All",
                              tristatevalue="x",
                              font=self.font, command=lambda: self.displayTask())
        # self.back = Button(self.scrollFrame.viewPort, text="Back", fg="peachpuff", bg="hotpink4", font=('Verdana', 10, 'bold'),
        #                  command=lambda: master.master.master.switch_frame(SchedulePage))
        # self.back.image=backicon
        self.displayTaskLabel = Label(self.scrollFrame.viewPort, font=("Verdana", "12", "bold"))
        # self.ntask = None
        # self.ndate = None
        # self.ntime = None


    def displayTaskAction(self):
        widget_list = all_children(self.scrollFrame)
        for item in widget_list:
            item.grid_forget()
        self.initTask()
        #self.renewButtonTask()
        self.displayTaskButton['bg'] = 'pink'
        self.displayTodoButton['bg'] = 'hotpink4'
        self.displayNoteButton['bg'] = 'hotpink4'
        self.display.grid(row=0, column=0, columnspan=5)
        self.R1.grid(row=1, column=0, columnspan=2,sticky=W)
        self.R2.grid(row=1, column=2, columnspan=3,sticky=W)
        self.R3.grid(row=2, column=0, columnspan=2,sticky=W)
        self.R4.grid(row=2, column=2, columnspan=3,sticky=W)
        #self.back.grid(row=3, column=0, columnspan=5)
        self.displayTaskLabel.grid(row=4, column=0, columnspan=5, pady=8)

    def displayTask(self):
        selection = self.radiovar.get()
        input = False
        # For specific Day only one speech input is taken
        if selection == "Specific Day":
            assistant_speaks("Please mention the day")
            date = get_audio()
            date = DateFromText(date)
            if date == None:
                input = False
            else:
                input = True
        # Two days taken as input (start and end date)
        elif selection == "Between two days":
            assistant_speaks("Please mention the start date")
            sdate = get_audio()
            sdate = DateFromText(sdate)
            assistant_speaks("Please mention the end date")
            edate = get_audio()
            edate = DateFromText(edate)
            if sdate == None or edate == None:
                input = False
            elif sdate>edate:
                input =False
                assistant_speaks("Start date cannot be greater than end date")
            else:
                input = True
        # No speech input for all upcoming or all tasks
        elif selection == "All Upcoming":
            today = datetime.date.today()
            input = True
        elif selection == "All":
            input = True

        # If speech input is identified and there are dates/days present in them
        if input == True:

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
                    query = "SELECT * FROM task WHERE date='" + date + "' ORDER BY time;"
                    selection = selection + " : " + date
                elif selection == "Between two days":
                    sdate = sdate.strftime("%Y-%m-%d")
                    edate = edate.strftime("%Y-%m-%d")
                    print("Start Date:", sdate, " End date:", edate)
                    query = "SELECT * FROM task WHERE date>='" + sdate + "' AND date<='" + edate + "' ORDER BY date,time;"
                    selection = " Between " + sdate + " and " + edate
                elif selection == "All Upcoming":
                    now = datetime.datetime.now()
                    today = now.strftime("%Y-%m-%d")
                    time_now = now.strftime("%H:%M:%S")
                    query = "SELECT * FROM task WHERE date>='" + today + "' ORDER BY date,time;"
                    selection = "All Upcoming Tasks"
                elif selection == "All":
                    query = "SELECT * FROM task ORDER BY date,time;"
                    selection = "All Tasks"
                self.displayTaskLabel.config(text=selection)
                cursor.execute(query)
                tasks = cursor.fetchall()
                # the data from db is display in grid with row>=5
                # First erase previous data
                for label in self.scrollFrame.viewPort.grid_slaves():
                    if int(label.grid_info()["row"]) >= 5:
                        label.grid_forget()
                index = 5
                if len(tasks) > 0:
                    stringtask = "Task-Id\t\tTask\t\tDate\t\tTime\n"
                    Label(self.scrollFrame.viewPort, text="Task", font=("Artefact", "12", "bold")).grid(row=index, column=0)
                    Label(self.scrollFrame.viewPort, text="Date", font=("Artefact", "12", "bold")).grid(row=index, column=1)
                    Label(self.scrollFrame.viewPort, text="Time", font=("Artefact", "12", "bold")).grid(row=index, column=2)

                    dimage = PhotoImage(file='images\delete.png')
                    deleteicon = dimage.subsample(10, 10)
                    eimage = PhotoImage(file='images\edit.png')
                    editicon = eimage.subsample(10, 10)
                    # each task is displayed in a row and a delete button is associated with it
                    for task in tasks:
                        index = index + 1
                        Label(self.scrollFrame.viewPort, text=task[1], font=self.font, padx=5, pady=5).grid(row=index, column=0,sticky=W)
                        Label(self.scrollFrame.viewPort, text=str(task[2]), font=self.font, padx=5, pady=5).grid(row=index, column=1,sticky=W)
                        Label(self.scrollFrame.viewPort, text=str(task[3]), font=self.font, padx=5, pady=5).grid(row=index, column=2,sticky=W)
                        d = Button(self.scrollFrame.viewPort, text="Delete", image=deleteicon,
                                   command=lambda id=task[0], row=index: self.deleteTask(id, row, index + 1))
                        d.image = deleteicon
                        d.grid(row=index, column=3)
                        e = Button(self.scrollFrame.viewPort, text="Edit", image=editicon,
                                   command=lambda id=task[0], row=index: self.displayEdit(id, row, index + 1))
                        e.image = editicon
                        e.grid(row=index, column=4)
                        stringtask += str(task[0]) + "\t\t" + task[1] + "\t\t" + str(task[2]) + "\t\t" + str(
                            task[3]) + "\n"
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
            self.displayTaskLabel.config(text="")
            assistant_speaks("Please repeat the process. Couldn't identify your audio or date mentioned")
            for label in self.scrollFrame.viewPort.grid_slaves():
                if int(label.grid_info()["row"]) >= 5:
                    label.grid_forget()

        # update width and height of the canvas self is frame which is binded to canvas.. so self.master is canvas
        self.master.update()
        self.master.configure(scrollregion=self.master.bbox("all"))

    def deleteTask(self, id, row, index):
        try:
            connection = psycopg2.connect(user="usertm",
                                          password="password",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="TaskManager")
            cursor = connection.cursor()
            query = "DELETE FROM task WHERE task_id=" + str(id) + ";"
            cursor.execute(query)
            for gridrow in self.scrollFrame.viewPort.grid_slaves():
                if int(gridrow.grid_info()["row"]) >= index:
                    gridrow.grid_forget()
            for label in self.scrollFrame.viewPort.grid_slaves():
                if int(label.grid_info()["row"]) == row:
                    label.grid_forget()
            assistant_speaks("Deletion Successful")
            connection.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            connection.rollback()
            print("Error while using PostgreSQL table", error)
        finally:
            # closing database connection.
            if (connection):
                cursor.close()
                connection.close()

        # update width and height of the canvas self is frame which is binded to canvas.. so self.master is canvas
        self.master.update()
        self.master.configure(scrollregion=self.master.bbox("all"))
        #self.displayTaskAction()

    def displayEdit(self, id, row, index):
        i = index
        try:
            connection = psycopg2.connect(user="usertm",
                                          password="password",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="TaskManager")
            cursor = connection.cursor()
            query = "SELECT * FROM task WHERE task_id=" + str(id) + ";"
            cursor.execute(query)
            task = cursor.fetchone()
            Label(self.scrollFrame.viewPort, text="").grid(row=i, column=0, columnspan=5)
            i += 1
            self.ntask = StringVar(value=task[1])
            self.ndate = StringVar(value=task[2])
            self.ntime = StringVar(value=task[3])
            Label(self.scrollFrame.viewPort, text="Task:", font=("Lucida Bright", "10", "bold")).grid(row=i, column=0, columnspan=2)
            self.inputTask = Entry(self.scrollFrame.viewPort, textvariable=self.ntask)
            self.inputTask.grid(row=i, column=2, columnspan=2)
            i += 1
            Label(self.scrollFrame.viewPort, text="Date:", font=("Lucida Bright", "10", "bold")).grid(row=i, column=0, columnspan=2)
            self.inputDate = Entry(self.scrollFrame.viewPort, textvariable=self.ndate)
            self.inputDate.grid(row=i, column=2, columnspan=2)
            i += 1
            Label(self.scrollFrame.viewPort, text="Time:", font=("Lucida Bright", "10", "bold")).grid(row=i, column=0, columnspan=2)
            self.inputTime = Entry(self.scrollFrame.viewPort, textvariable=self.ntime)
            self.inputTime.grid(row=i, column=2, columnspan=2)
            i += 1
            mike = PhotoImage(file='images\mike5.png')
            mike = mike.subsample(25, 20)
            mikeButton = Button(self.scrollFrame.viewPort, image=mike,
                                command=lambda: self.speakTask())
            mikeButton.image = mike
            mikeButton.grid(row=i, column=1)

            simage = PhotoImage(file='images\save_edit.png')
            saveicon = simage.subsample(10, 10)
            s = Button(self.scrollFrame.viewPort, text="Save Changes", font=("Lucida Bright", "10", "bold"), image=saveicon, compound=LEFT,
                       command=lambda: self.editTask(id, row, index))
            s.image = saveicon
            s.grid(row=i, column=2, columnspan=3)
            assistant_speaks("Task details are displayed for editing")
            connection.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            connection.rollback()
            print("Error while using PostgreSQL table", error)
        finally:
            # closing database connection.
            if (connection):
                cursor.close()
                connection.close()
        # update width of the canvas self is frame which is binded to canvas.. so self.master is canvas
        self.master.update()
        self.master.configure(scrollregion=self.master.bbox("all"))

    def speakTask(self):
        assistant_speaks("Is there any change in task?")
        text = get_audio()
        if text is not None:
            text = text.lower()
            if text.count("yes") > 0:
                assistant_speaks("Please specify the task")
                text = get_audio()
                if text is not None:
                    self.ntask.set(text)
        assistant_speaks("Is there any change in date?")
        text = get_audio()
        if text is not None:
            text = text.lower()
            if text.count("yes") > 0:
                assistant_speaks("Please specify the day")
                text = get_audio()
                tdate = DateFromText(text)  # get date from text
                if tdate is not None:
                    self.ndate.set(tdate)
        assistant_speaks("Is there any change in time?")
        text = get_audio()
        if text is not None:
            text = text.lower()
            if text.count("yes") > 0:
                assistant_speaks("Please specify the time")
                text = get_audio()
                time = TimeFromText(text)  # get time from text
                if time is not None:
                    self.ntime.set(time)

    def editTask(self, id, row, index):
        try:
            connection = psycopg2.connect(user="usertm",
                                          password="password",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="TaskManager")
            cursor = connection.cursor()
            cursor = connection.cursor()
            task = self.inputTask.get()
            print(task)
            date = self.inputDate.get()
            print(date)
            time = self.inputTime.get()
            print(time)
            if len(task)!=0 and len(date)!=0:
                if len(time)!=0:
                    query = "UPDATE task SET task='" + task + "',date='" + date + "',time='" + time + "' WHERE task_id=" + str(
                    id) + ";"
                else:
                    query = "UPDATE task SET task='" + task + "',date='" + date + "',time=NULL WHERE task_id=" + str(
                        id) + ";"
                cursor.execute(query)
                for gridrow in self.scrollFrame.viewPort.grid_slaves():
                    if int(gridrow.grid_info()["row"]) >= index:
                        gridrow.grid_forget()
                for label in self.scrollFrame.viewPort.grid_slaves():
                    if int(label.grid_info()["row"])==row and int(label.grid_info()["column"])<=2:
                        label.grid_forget()
                Label(self.scrollFrame.viewPort,font=self.font, text=task).grid(row=row, column=0)
                Label(self.scrollFrame.viewPort, font=self.font,text=date).grid(row=row, column=1)
                Label(self.scrollFrame.viewPort,font=self.font, text=time).grid(row=row, column=2)
                assistant_speaks("Task edited successfully")
                connection.commit()
            elif len(task)==0:
                assistant_speaks("Please enter task")
            elif len(date)==0:
                assistant_speaks("Please enter date")
        except (Exception, psycopg2.DatabaseError) as error:
            connection.rollback()
            print("Error while using PostgreSQL table", error)
        finally:
            # closing database connection.
            if (connection):
                cursor.close()
                connection.close()
        # update width of the canvas self is frame which is binded to canvas.. so self.master is canvas
        self.master.update()
        self.master.configure(scrollregion=self.master.bbox("all"))

    def initTodo(self):
        self.backinner = Button(self.scrollFrame.viewPort, text="Back", width=4,
                                fg="white", bg="hotpink4", relief="ridge", font=('Verdana', 15),
                                command=lambda: self.backAction())
        self.add = Button(self.scrollFrame.viewPort, text="+", width=10,
                          fg="white", bg="hotpink4", relief="ridge", font=('Verdana', 15),
                          command=lambda: self.addNewFile())
        self.inputNew = Entry(self.scrollFrame.viewPort, width=30,
                              fg="white", bg="hotpink4", relief="ridge", font=('Verdana', 15))
        self.tempButton = Button(self.scrollFrame.viewPort, text="Add", width=3,
                                 fg="white", bg="hotpink4", relief="ridge", font=('Verdana', 15),
                                 command=lambda: self.addSubmit())
        self.checkbuttons = []
        self.checkvalues = []
        self.file = None

    def displayTodoAction(self):
        widget_list = all_children(self.scrollFrame)
        for item in widget_list:
            item.grid_forget()
        self.displayTaskButton['bg'] = 'hotpink4'
        self.displayTodoButton['bg'] = 'pink'
        self.displayNoteButton['bg'] = 'hotpink4'
        self.printData()

    def backAction(self):
        self.file = None
        self.printData()

    def renewButton(self):
        self.backinner = Button(self.scrollFrame.viewPort, text="Back", width=4,
                                fg="white", bg="hotpink4", relief="ridge", font=('Verdana', 10),
                                command=lambda: self.backAction())
        self.add = Button(self.scrollFrame.viewPort, text="+", width=10,
                          fg="white", bg="hotpink4", relief="ridge", font=('Verdana', 10),
                          command=lambda: self.addNewFile())
        self.inputNew = Entry(self.scrollFrame.viewPort, width=15,
                              fg="hotpink4",bd=2, relief="ridge", font=('Verdana', 15))
        self.tempButton = Button(self.scrollFrame.viewPort, text="Add", width=3,
                                 fg="white", bg="hotpink4", relief="ridge", font=('Verdana', 10),
                                 command=lambda: self.addSubmit())
        self.add.grid(row=0, column=0)
        if self.file is not None:
            self.backinner.grid(row=0, column=1)

    def printData(self):
        widget_list = all_children(self.scrollFrame)
        for item in widget_list:
            item.grid_forget()
        self.scrollFrame.pack_forget()
        self.scrollFrame = None
        self.scrollFrame = ScrollFrame(self.displayAll, 425, 425)
        self.scrollFrame.pack(side="top", fill="both", expand=True)
        self.renewButton()
        try:
            connection = psycopg2.connect(user="usertm",
                                          password="password",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="TaskManager")
            cursor = connection.cursor()
            if self.file is None:
                str = "select list_name from todo_list_name"
                cursor.execute(str)
                rows = cursor.fetchall()
                i = 2
                for row in rows:
                    a = row[0]
                    Button(self.scrollFrame.viewPort, text=row[0], fg="hotpink4", borderwidth=2, width=19,
                          relief="ridge", font=('Verdana', 15), command=lambda x=a: self.displayList(x)).grid(
                        row=i, column=0)
                    Button(self.scrollFrame.viewPort, text="x", fg="white", background="red", borderwidth=2, width=3,
                          relief="ridge", font=('Verdana', 15), command=lambda x=a: self.removeFile(x)).grid(
                        row=i, column=1)
                    i += 1
            else:
                str = "select todo_name,completed from todo_names where list_name = '%s'"
                args = self.file
                cursor.execute(str % args)
                rows = cursor.fetchall()
                Label(self.scrollFrame.viewPort, text=self.file, fg="hotpink4", borderwidth=2, width=18,
                          relief="ridge", font=('Verdana', 15, 'bold')).grid(row=2, column=0)
                i = 3
                self.checkbuttons = []
                self.checkvalues = []
                for row in rows:
                    a = row[0]
                    self.checkvalues.append(BooleanVar())
                    if row[1] == FALSE:
                        self.checkbuttons.append(
                            Checkbutton(self.scrollFrame.viewPort, text=f'{row[0]}', variable=self.checkvalues[i - 3],
                                        onvalue=True,
                                        offvalue=False, fg='hotpink4', width=28, font=('Verdana', 10), command=lambda x=a: self.selectTodo(x)))
                    else:
                        self.checkvalues[i - 3].set(True)
                        self.checkbuttons.append(
                            Checkbutton(self.scrollFrame.viewPort, text=f'{row[0]}', variable=self.checkvalues[i - 3],
                                        onvalue=True,
                                        offvalue=False, fg='hotpink4', width=28, font=('Verdana', 10), command=lambda x=a: self.deselectTodo(x)))
                    self.checkbuttons[i - 3].grid(row=i + 1, column=0, sticky=W)
                    Button(self.scrollFrame.viewPort, text="x", fg='white',background="red", width=5, font=('Verdana', 10), command=lambda x=a: self.remove(x)).grid(
                        row=i + 1, column=1)
                    i += 1
        except (Exception, psycopg2.DatabaseError) as error:
            connection.rollback()
            print("Error while using PostgresSQL table", error)
        finally:
            # closing database connection.
            if connection:
                cursor.close()
                connection.close()

    def displayList(self, list_name):
        self.file = list_name
        self.printData()

    def addNewFile(self):
        self.inputNew.grid(row=1, column=0)
        self.tempButton.grid(row=1, column=1)

    def addSubmit(self):
        if self.file is None:
            todoDbAction("Create", None, self.inputNew.get())
            self.file = self.inputNew.get()
        else:
            todoDbAction("Add", self.inputNew.get(), self.file)
        self.inputNew.grid_forget()
        self.tempButton.grid_forget()
        self.inputNew.delete(0, END)
        self.printData()

    def removeFile(self, text):
        todoDbAction('Delete', None, text)
        todoDbAction('Clear All', None, text)
        self.printData()

    def selectTodo(self, text):
        todoDbAction('Check', text, self.file)
        self.printData()

    def deselectTodo(self, text):
        todoDbAction('Uncheck', text, self.file)
        self.printData()

    def remove(self, text):
        todoDbAction('Delete', text, self.file)
        self.printData()

    def initNote(self):
        self.display = Label(self.scrollFrame.viewPort, text="Notes created", font=("calibri", 12, "bold"))
        self.display1 = Label(self.scrollFrame.viewPort, text="Date created", font=("calibri", 12, "bold"))
        self.display2 = Label(self.scrollFrame.viewPort, text="Last modified", font=("calibri", 12, "bold"))
        self.font = ("calibri", "11")
        self.radiovar = StringVar()

    def displayNoteAction(self):
        widget_list = all_children(self.scrollFrame)
        for item in widget_list:
            item.grid_forget()
        self.initNote()
        self.displayTaskButton['bg'] = 'hotpink4'
        self.displayTodoButton['bg'] = 'hotpink4'
        self.displayNoteButton['bg'] = 'pink'
        self.display.grid(row=1, column=0)
        self.display1.grid(row=1, column=1)
        self.display2.grid(row=1, column=2)
        self.displayNoteInFrame()

    def displayNoteInFrame(self):
        try:
            connection = psycopg2.connect(user="usertm",
                                          password="password",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="TaskManager")
            cursor = connection.cursor()
            query = "SELECT note_id, title,date_created,date_modified from note ORDER BY date_modified DESC;"
            cursor.execute(query)
            data = cursor.fetchall()
            i = 2
            for title in data:
                Radiobutton(self.scrollFrame.viewPort, text=title[1], font=self.font, padx=5, pady=5, variable=self.radiovar,
                            tristatevalue='x', value=title[0],
                            command=lambda row=i: self.displayNote(row, i + 1)).grid(row=i, column=0,sticky=W)
                Label(self.scrollFrame.viewPort, text=title[2].strftime('%Y-%m-%d %H:%M'), font=self.font,padx=5,pady=5).grid(row=i, column=1,sticky=W)
                Label(self.scrollFrame.viewPort, text=title[3].strftime('%Y-%m-%d %H:%M'), font=self.font,padx=5,pady=5).grid(row=i, column=2, sticky=W)
                i = i + 1
            connection.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            connection.rollback()
            print("Error while using PostgreSQL table", error)
        finally:
            # closing database connection.
            if (connection):
                cursor.close()
                connection.close()

    def displayNote(self,row,index):
        note_index=index
        try:
            note_id = self.radiovar.get()
            connection = psycopg2.connect(user="usertm",
                                          password="password",
                                            host="127.0.0.1",
                                              port="5432",
                                              database="TaskManager")
            cursor = connection.cursor()
            query = "SELECT * FROM note WHERE note_id='"+note_id+"' ORDER BY date_modified DESC;"
            cursor.execute(query)
            notes=cursor.fetchone()
             # the data from db is display in grid with row>=5
            # First erase previous data
            for label in self.scrollFrame.viewPort.grid_slaves():
                if int(label.grid_info()["row"]) >= note_index:
                    label.grid_forget()
            self.mikeTodo = PhotoImage(file='images\mike5.png')
            self.speakicon = self.mikeTodo.subsample(25, 20)
            self.title = StringVar(value=notes[4])

            Label(self.scrollFrame.viewPort, text="Title:", font=("Lucida Bright", "10", "bold")).grid(row=index, column=0)
            self.inputTitle = Entry(self.scrollFrame.viewPort, textvariable=self.title)
            self.inputTitle.grid(row=index, column=1, columnspan=2)

            self.s = Button(self.scrollFrame.viewPort, image=self.speakicon, compound=LEFT,
                            command=lambda: self.actionSpeakNoteTitle())
            self.s.image = self.speakicon
            self.s.grid(row=index, column=3, padx=5, ipadx=3)
            index += 1
            Label(self.scrollFrame.viewPort, text="Note:", font=("Lucida Bright", "10", "bold")).grid(row=index, column=0)
            self.inputNote=Text(self.scrollFrame.viewPort,height=5,width=20)
            self.inputNote.grid(row=index, column=1, columnspan=2)
            self.inputNote.delete(1.0, END)
            self.inputNote.insert(END, notes[1])
            self.s = Button(self.scrollFrame.viewPort, image=self.speakicon, compound=LEFT,
                            command=lambda: self.actionSpeakNote())
            self.s.image = self.speakicon
            self.s.grid(row=index, column=3, padx=5, ipadx=3)
            index += 1
            # Label(self, text=title,font=("Artefact","12","bold")).grid(row=index, column=0)
            # Label(self,font=("Artefact","12","bold")).grid(row=index+1, column=0)
            #Label(self, text="Date and Time created",font=("Artefact","12","bold")).grid(row=index, column=2)
            dimage = PhotoImage(file='images\delete_1.png')
            deleteicon = dimage.subsample(20, 20)
            eimage = PhotoImage(file='images\edit_1.png')
            editicon = eimage.subsample(20, 20)
            d=Button(self.scrollFrame.viewPort,text="Delete",image=deleteicon, command=lambda id=notes[0]: self.deleteNote(id,row,note_index))
            d.image = deleteicon
            d.grid(row=index, column=1)
            e = Button(self.scrollFrame.viewPort, text="Edit", image=editicon,command=lambda id=notes[0]: self.editNote(id,row,note_index))
            e.image = editicon
            e.grid(row=index, column=2)
            #stringnote +=str(note[0])+"\t\t"+note[1]+"\t\t"+str(note[2])+"\t\t"+str(note[3])+"\n"
            #print(stringnote)
            assistant_speaks("The Note is displayed")
            connection.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            connection.rollback()
            print("Error while using PostgreSQL table", error)
        finally:
           # closing database connection.
            if (connection):
                cursor.close()
                connection.close()
        # update width and height of the canvas self is frame which is binded to canvas.. so self.master is canvas
        self.master.update()
        self.master.configure(scrollregion=self.master.bbox("all"))

    def deleteNote(self,id,row,index):
        try:
            connection = psycopg2.connect(user="usertm",
                                          password="password",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="TaskManager")
            cursor = connection.cursor()
            query="DELETE FROM note WHERE note_id="+str(id)+";"
            cursor.execute(query)
            for gridrow in self.scrollFrame.viewPort.grid_slaves():
                if int(gridrow.grid_info()["row"]) >= index:
                    gridrow.grid_forget()
            for label in self.scrollFrame.viewPort.grid_slaves():
                if int(label.grid_info()["row"])==row:
                    label.grid_forget()
            assistant_speaks("Note deleted successfully")
            connection.commit()
        except (Exception , psycopg2.DatabaseError) as error:
            connection.rollback()
            print("Error while using PostgreSQL table", error)
        finally:
        # closing database connection.
            if (connection):
                cursor.close()
                connection.close()
        # update width and height of the canvas self is frame which is binded to canvas.. so self.master is canvas
        self.master.update()
        self.master.configure(scrollregion=self.master.bbox("all"))

    def editNote(self,id,row,index):
        try:
            connection = psycopg2.connect(user="usertm",
                                          password="password",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="TaskManager")
            cursor = connection.cursor()
            cursor = connection.cursor()
            title= self.inputTitle.get()
            note = self.inputNote.get("1.0",END)
            print(len(self.inputNote.get("1.0","end-1c")))
            if len(self.inputNote.get("1.0","end-1c"))!=0:
                now = datetime.datetime.now()
                date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
                print(date_time)
                query = "UPDATE note SET title='" + title + "',note='" + note +"',date_modified='"+date_time+"' WHERE note_id="+str(id)+";"
                cursor.execute(query)
                assistant_speaks("Note edited successfully")
                connection.commit()
                self.initNote()
                self.displayNoteAction()
            else:
                assistant_speaks("Note cannot be empty")
        except (Exception , psycopg2.DatabaseError) as error:
            connection.rollback()
            print("Error while using PostgreSQL table", error)
        finally:
        # closing database connection.
            if (connection):
                cursor.close()
                connection.close()
        # update width of the canvas self is frame which is binded to canvas.. so self.master is canvas
        self.master.update()
        self.master.configure(scrollregion=self.master.bbox("all"))

    def actionSpeakNoteTitle(self):
        self.inputTitle.delete(0, END)
        assistant_speaks("Please specify the title of note")
        text = get_audio()
        self.title.set(text)
        print(text)

    def actionSpeakNote(self):
        #self.inputNote.delete(0, END)
        assistant_speaks('Please specify the note to be changed')
        voice = get_audio()
        self.inputNote.insert(END,voice)
        print(self.inputNote.get("1.0",END))


class DisplayNotePage(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.back = Button(self, text="Back",
                           fg="peachpuff", bg="hotpink4",
                           font=('Verdana', 10, 'bold'),
                           command=lambda: master.switch_frame(SchedulePage))
        self.back.grid(row=0, column=0)


class HelpPage(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.back = Button(self, text="Back",
                           fg="white", bg="DeepPink2",
                           command=lambda: master.switch_frame(SchedulePage))
        self.back.grid(row=0, column=0)
