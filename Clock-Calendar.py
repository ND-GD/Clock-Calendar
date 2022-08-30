from tkinter import *
from time import *

def Calendar():
    timeText = strftime("%I:%M:%S %p")
    timeField.config(text=timeText)

    dayText = strftime("%A")
    dayField.config(text=dayText)

    dateText = strftime("%B %d %Y")
    dateField.config(text=dateText)

    timeField.after(1000, Calendar)

onlyWindow = Tk()
onlyWindow.title("Calendar")

timeField = Label(onlyWindow, font=("Times New Roman",40),fg="black", bg="white")
timeField.pack()

dayField = Label(onlyWindow, font=("Times New Roman",30),fg="black", bg="white")
dayField.pack()

dateField = Label(onlyWindow, font=("Times New Roman",30),fg="black", bg="white")
dateField.pack()

Calendar()

onlyWindow.mainloop()