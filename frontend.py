from tkinter import *

# Create empty window
window = Tk()

# Add execute button widget
b1 = Button(window, text="Execute")
b1.grid(row = 0, column = 0)

# Add text entry widget
e1 = Entry(window)
e1.grid(row = 0, column = 1)

window.mainloop()