from tkinter import *
from tkinter import ttk
from functools import partial

y = 0
x = 0
operation = 0
operatorpressed = False


def calculate():
    global operation
    global x
    global y

    if(operatorpressed == True):
        if operation == 0:
            y *= x
            x = 0
            a.set(y)
        if operation == 1:
            y /= x
            x = 0
            a.set(y)
        if operation == 2:
            y += x
            x = 0
            a.set(y)
        if operation == 3:
            y -= x
            x = 0
            a.set(y)
        

def setNums(n):
    global y
    global x
    global operatorpressed
    if(operatorpressed == False):
        y *= 10
        y += n
        a.set(y)
    else:
        x *= 10
        x += n
        a.set(x)
        

def setOperators(n):
    global operation
    global operatorpressed
    operation = n
    operatorpressed = True


root = Tk()
root.title("Calculator")
root.resizable(False, False)


mainframe = ttk.Frame(root, padding = "5 5 12 12")
mainframe.grid(column = 0, row = 0, sticky = (N, W, E, S))
root.columnconfigure(0, weight = 1)
root.rowconfigure(0, weight = 1)


a = StringVar()
ttk.Label(mainframe, textvariable = a).grid(column = 2, row = 0, sticky = N)
ttk.Button(mainframe, text="=", command=calculate).grid(column = 5, row = 4, sticky=(S, W))

ttk.Button(mainframe, text=str(1), command=partial(setNums, 1)).grid(column = 0, row = 4, sticky=(S, E))
ttk.Button(mainframe, text=str(2), command=partial(setNums, 2)).grid(column = 1, row = 4, sticky=(S, E))
ttk.Button(mainframe, text=str(3), command=partial(setNums, 3)).grid(column = 2, row = 4, sticky=(S, E))
ttk.Button(mainframe, text=str(4), command=partial(setNums, 4)).grid(column = 0, row = 3, sticky=(S, E))
ttk.Button(mainframe, text=str(5), command=partial(setNums, 5)).grid(column = 1, row = 3, sticky=(S, E))
ttk.Button(mainframe, text=str(6), command=partial(setNums, 6)).grid(column = 2, row = 3, sticky=(S, E))
ttk.Button(mainframe, text=str(7), command=partial(setNums, 7)).grid(column = 0, row = 2, sticky=(S, E))
ttk.Button(mainframe, text=str(8), command=partial(setNums, 8)).grid(column = 1, row = 2, sticky=(S, E))
ttk.Button(mainframe, text=str(9), command=partial(setNums, 9)).grid(column = 2, row = 2, sticky=(S, E))
ttk.Button(mainframe, text=str(0), command=partial(setNums, 0)).grid(column = 5, row = 3, sticky=(S, E))

ttk.Button(mainframe, text="X", command=partial(setOperators, 0)).grid(column = 4, row = 3, sticky=(S, W))
ttk.Button(mainframe, text="/", command=partial(setOperators, 1)).grid(column = 4, row = 4, sticky=(S, W))
ttk.Button(mainframe, text="+", command=partial(setOperators, 2)).grid(column = 3, row = 3, sticky=(S, W))
ttk.Button(mainframe, text="-", command=partial(setOperators, 3)).grid(column = 3, row = 4, sticky=(S, W))

root.bind("<Return>", calculate)
root.mainloop()