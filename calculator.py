from tkinter import *
from tkinter import ttk
from turtle import window_width

class Calculator:

    def __init__(self, root):

        root.title("Calculator")
        # change window icon
        # root.iconbitmap("codemy.ico")

        mainframe = ttk.Frame(root, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        self.entry_value = StringVar()
        self.entry_value.set('0')

        self.which_operation = 0

        self.first_value = 0
        self.second_value = 0

        self.entry = ttk.Label(mainframe, textvariable=self.entry_value, background='LightGray', anchor='e', font=("Arial", 20))
        self.entry.grid(column=0, row=0, sticky=(W, E), columnspan=4, rowspan=2)

        ttk.Button(mainframe, text="7", command=lambda: self.Press(7)).grid(column=0, row=2, sticky=W)
        ttk.Button(mainframe, text="8", command=lambda: self.Press(8)).grid(column=1, row=2, sticky=W)
        ttk.Button(mainframe, text="9", command=lambda: self.Press(9)).grid(column=2, row=2, sticky=W)
        ttk.Button(mainframe, text="4", command=lambda: self.Press(4)).grid(column=0, row=3, sticky=W)
        ttk.Button(mainframe, text="5", command=lambda: self.Press(5)).grid(column=1, row=3, sticky=W)
        ttk.Button(mainframe, text="6", command=lambda: self.Press(6)).grid(column=2, row=3, sticky=W)
        ttk.Button(mainframe, text="1", command=lambda: self.Press(1)).grid(column=0, row=4, sticky=W)
        ttk.Button(mainframe, text="2", command=lambda: self.Press(2)).grid(column=1, row=4, sticky=W)
        ttk.Button(mainframe, text="3", command=lambda: self.Press(3)).grid(column=2, row=4, sticky=W)
        ttk.Button(mainframe, text="0", command=lambda: self.Press(0)).grid(column=1, row=5, sticky=W)

        ttk.Button(mainframe, text="CLR", command=self.Clear).grid(column=0, row=5, sticky=W)
        ttk.Button(mainframe, text="+-", command=self.SwitchSign).grid(column=2, row=5, sticky=W)

        ttk.Button(mainframe, text="*", command=lambda: self.SetVal(3)).grid(column=3, row=2, sticky=W)
        ttk.Button(mainframe, text="/", command=lambda: self.SetVal(2)).grid(column=3, row=3, sticky=W)
        ttk.Button(mainframe, text="-", command=lambda: self.SetVal(1)).grid(column=3, row=4, sticky=W)
        ttk.Button(mainframe, text="+", command=lambda: self.SetVal(0)).grid(column=3, row=5, sticky=W)
        
        ttk.Button(mainframe, text="=", command=self.Compute).grid(column=3, row=6, sticky=W)

        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)
        
        self.entry.focus()

        root.bind("<Return>", self.Compute)

    def Clear(self):
        self.entry_value.set('0')
        self.first_value = 0
        self.second_value = 0

    def SwitchSign(self):
        num = int(self.entry_value.get())
        self.entry_value.set(str(-num))

    def Press(self, num):
        curr = int(self.entry_value.get())
        curr *= 10
        curr += num
        self.entry_value.set(str(curr))

    def SetVal(self, oper):
        try:
            self.which_operation = oper # set operation value
            self.first_value = int(self.entry_value.get()) # set first value
            self.entry_value.set("0") # clear entry

            self.entry.focus() # focus on entry
        except ValueError:
            pass

    def Compute(self, *args):
        try:
            if self.which_operation == 0:
                self.second_value = int(self.entry_value.get())
                self.entry_value.set(str(self.first_value + self.second_value))
            elif self.which_operation == 1:
                self.second_value = int(self.entry_value.get())
                self.entry_value.set(str(self.first_value - self.second_value))
            elif self.which_operation == 2:
                self.second_value = int(self.entry_value.get())
                self.entry_value.set(str(self.first_value / self.second_value))
            elif self.which_operation == 3:
                self.second_value = int(self.entry_value.get())
                self.entry_value.set(str(self.first_value * self.second_value))

        except ValueError:
            self.entry_value.set("Error")
            pass

root = Tk()
Calculator(root)
root.mainloop()