from tkinter import *

# import our class and functions
from startPage import StartPage


class mainApp(Tk):
    def __init__(self):
        Tk.__init__(self)

        self._frame = None
        self.frame_canvas = Frame(self, bg="gray")
        self.frame_canvas.grid(sticky='news')
        self.frame_canvas.grid_rowconfigure(0, weight=1)
        self.frame_canvas.grid_columnconfigure(0, weight=1)
        # Set grid_propagate to False to allow 5-by-5 buttons resizing later
        self.frame_canvas.grid_propagate(False)
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        # Add a canvas in that frame
        canvas = Canvas(self.frame_canvas)
        canvas.grid(row=0, column=0, sticky="news")

        # Link a scrollbar to the canvas
        vsb = Scrollbar(self.frame_canvas, orient="vertical", command=canvas.yview)
        vsb.grid(row=0, column=1, sticky='ns')
        vsb.config(command=canvas.yview)
        canvas.config(yscrollcommand=vsb.set)

        new_frame = frame_class(canvas)
        # Create a frame to contain the buttons
        canvas.create_window((0, 0), window=new_frame, anchor='nw')
        new_frame.update_idletasks()

        if self.frame_canvas is not None:
            self.frame_canvas.config(width=300,height=375)
        canvas.config(scrollregion=canvas.bbox("all"))

        """Destroys current frame and replaces it with a new one."""
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        #self._frame.pack()



if __name__ == "__main__":
    root = mainApp()
    root.title("Task Manager")
    root.geometry("300x375")
    root.configure(background="gray20")
    root.grid_rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)
    root.mainloop()