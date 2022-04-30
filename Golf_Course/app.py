from email import message
from tkinter import *
from tkinter import scrolledtext
from solution1 import *
import re


class Golf_App(Tk):
    def __init__(self):
        super().__init__()
        self.title("Golf Schedule")
        self.iconbitmap("data/golf_icon.ico")

        self.time_label = Label(self, text= "Tee Time: (HH:MM)")
        self.time_input = Entry(self, width=13)
        self.course_label = Label(self, text= "Course:")

        self.course_input = StringVar()
        self.course_buttons = []
        for course_name in ['Augusta', 'Laguna', 'Pebble Bay']:
            button = Radiobutton(self, text = course_name, variable = self.course_input, value= course_name)
            self.course_buttons.append(button)

        self.schedule_button = Button(self, text = "Show Schedule", relief=RAISED, command=self.get_schedule)
        self.clear_button = Button(self, text = "Clear", state = DISABLED, relief=RAISED, width=13, command=self.clear)
        self.text_field = scrolledtext.ScrolledText(self, width=50,  height=25)


        self.time_label.grid(row=0, column=0, padx=(10,0), pady=5)
        self.time_input.grid(row=0, column=1, padx=0, pady=0, sticky=W)
        self.course_label.grid(row=1, column=0, padx=(45,0), sticky=W)
        for i in range(3):
            self.course_buttons[i].grid(row=1+i, column=1, sticky=W)

        self.course_input.set('Augusta')
        self.schedule_button.grid(row=4, column=0)
        self.clear_button.grid(row=4, column=1, sticky=W, pady=(5,0))
        self.text_field.grid(row=5, column=0, columnspan=3, padx=5, pady=20)

    def get_schedule(self):
        teeTime = self.time_input.get()
        
        if not ((re.search("^[0-2][0-9]:[0-5][0-9]$", teeTime)) and (int(teeTime[:2]) < 24)):
            message = "Please enter time in HH:MM format..."
        
        else:
            filename = "data/" + self.course_input.get() + ".txt"
            course = Course(filename)

            hr, mi = [int(i) for i in teeTime.split(":")]
            message = course.getPlaySchedule(datetime(2001, 1, 1, hr, mi))
        
        self.clear_button["state"] = 'normal'
        self.time_input.delete(0, END)

        prev_msg = self.text_field.get("1.0", END) + '\n'
        self.text_field.delete("1.0", END)
        prev_msg = prev_msg.lstrip()
        self.text_field.insert(INSERT, prev_msg + message)
        

    def clear(self):
        self.text_field.delete("1.0", END)
        self.clear_button["state"] = 'disabled'
        self.time_input.delete(0, END)
        self.course_input.set('Augusta')


if __name__ == '__main__':
    app = Golf_App()
    app.mainloop()