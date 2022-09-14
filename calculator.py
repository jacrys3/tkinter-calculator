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

        self.which_operation = 0

        self.first_value = 0
        self.second_value = 0

        self.entry = ttk.Entry(mainframe, textvariable=self.entry_value, background='DarkOrchid', width=10, justify='right')
        self.entry.grid(column=0, row=0, sticky=(W, E), columnspan=3, rowspan=2)

        ttk.Frame(mainframe, width=150, height=200, relief='ridge').grid(column=0, row=2, columnspan=2, rowspan=5)

        ttk.Button(mainframe, text="*", command=lambda: self.SetVal(3)).grid(column=2, row=2, sticky=W)
        ttk.Button(mainframe, text="/", command=lambda: self.SetVal(2)).grid(column=2, row=3, sticky=W)
        ttk.Button(mainframe, text="-", command=lambda: self.SetVal(1)).grid(column=2, row=4, sticky=W)
        ttk.Button(mainframe, text="+", command=lambda: self.SetVal(0)).grid(column=2, row=5, sticky=W)
        
        ttk.Button(mainframe, text="=", command=self.Compute).grid(column=2, row=6, sticky=W)

        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)
        
        self.entry.focus()

        root.bind("<Return>", self.Compute)

    def SetVal(self, oper):
        try:
            self.which_operation = oper # set operation value
            self.first_value = int(self.entry_value.get()) # set first value
            self.entry_value.set("") # clear entry

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