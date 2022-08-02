#A text file is created with the inputed text added to it.
# The name of the file is the date the journal was used.
# If the user enters several texts in a day, these texts are appended at the end of each other.

from datetime import date
import os.path
import tkinter as tk

#make text file with the date as the name
def makeFile(text):
    fileName = str(date.today())+".txt"
    path = "/Users/adeltazhibi/Desktop/Journal";
    filePath = os.path.join(path,fileName)
    if os.path.exists(filePath):
        with open(filePath, 'a') as f:
            f.write("\n\n")
            f.write(text)
            lbl.config(text="Added to the already made file!")
    else:
        with open(filePath, 'w') as f:
            f.write(text)
            lbl.config(text="File created!")


# Top level window
frame = tk.Tk()
frame.title("Daily Journal")
frame.geometry('600x340')


# Function for getting Input
# from textbox and calling makeFile()
def buttonAction():
    inp = inputtxt.get(1.0, "end-1c")
    # lbl.config(text="File created!")
    makeFile(inp)

# TextBox Creation
inputtxt = tk.Text(frame,
                   height=20,
                   width=100)
inputtxt.pack()

# Button Creation
createFileButton = tk.Button(frame,
                        text="Create",
                        command=buttonAction,width=10,height=2)
createFileButton.pack()

# Label Creation
lbl = tk.Label(frame, text="")
lbl.pack()
frame.mainloop()
