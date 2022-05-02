import tkinter as tk
from tkinter import filedialog, Text    
import os

# this will hold whole app
root = tk.TK()

canvas = tk.Canvas(root, height=700, width=700, bg="#263D42")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

# specify initial directory
def addApp():
    filename= filedialog.askopenfilename(initialdir="/", title="Select File",
                                                filetypes=(("exectuables", "*exe"), ("all files", "*.*")))

# add button
# can also add to frame but in this case attach to root
# fg or foreground refers test in this case
# command links the defined function addApp
openFile = tk.Button(root, text="Open File", padx=10, 
                     pady=5, fg="white", bg="#263D42", command=addApp)
# attaches button 
openFile.pack()

runApps = tk.Button(root, text="Run Apps", padx=10, pady=5, fg="white", bg="#263D42")
runApps.pack()


# this will run whole app
root.mainloop()

