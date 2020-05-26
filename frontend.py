from tkinter import *

# Create empty window
window = Tk()

def print_thing():
    # Delete previous text from t1:
    t1.delete(1.0, END)
    # Insert entry text into t1:
    t1.insert(END, e1_value.get())

# Add execute button widget
b1 = Button(window, text="Execute", command = print_thing)
b1.grid(row = 0, column = 0)

# Add text entry widget
e1_value = StringVar()
e1 = Entry(window, textvariable = e1_value)
e1.grid(row = 0, column = 1)

# Add text widget
t1 = Text(window, height = 1, width = 20)
t1.grid(row = 0, column = 2)

window.mainloop()