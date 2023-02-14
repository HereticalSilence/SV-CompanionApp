"""
Stardew Valley Companion App - Companion App.py

A companion app for the popular game Stardew Valley, created by ConcernedApe.
It features a planning calendar, profit calculator and look up tool for Crops, Animals and NPCs.

Credit to Github users
Exnil for their Crop Planner
https://exnil.github.io/crop_planner/

Thorinair for their Profit Calculator
https://thorinair.github.io/Stardew-Profits/

which served as inspiration for this program

Author: HereticalSilence
"""


from tkinter import * #Import TK
import tkinter as tkinter
from tkinter import ttk

#Define week days and seasons list
weekList = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
seasons = []

def createBlankCalendar(tabToCreateAt):
    mainFrame = ttk.Frame(master=tabToCreateAt)
    for x in range(7):
        for y in range(5):
            frameGrid = ttk.Frame(master=mainFrame, relief=tkinter.RAISED, borderwidth=2, width=125, height=125)
            frameGrid.pack_propagate(False)
            frameGrid.grid(row=y, column=x)
            labelGrid = ttk.Label(master=frameGrid, text=f"Row No. {x}\nColumn No. {y}").pack()
    mainFrame.pack()



root = Tk() #Create root window
root.resizable(width=False, height=False)
root.title("Stardew Valley Companion App") #Assign window title
root.geometry('1280x720') #Set window size 

menu = Menu(root)
item = Menu(menu)
item.add_command(label='Save')
item.add_command(label='Load')
menu.add_cascade(label='File', menu=item)
root.config(menu=menu)



mainTabControl = ttk.Notebook




#Calendar Code#
calendarFrame = ttk.LabelFrame(master=root, relief=tkinter.RAISED, text="Calendar")
#Create Seasonal Tabs
calendarTabControl = ttk.Notebook(calendarFrame)
springTab = ttk.Frame(calendarTabControl)
summerTab = ttk.Frame(calendarTabControl)
fallTab = ttk.Frame(calendarTabControl)
winterTab = ttk.Frame(calendarTabControl)

#Add tabs to notebook
calendarTabControl.add(springTab, text="Spring")
calendarTabControl.add(summerTab, text="Summer")
calendarTabControl.add(fallTab, text="Fall")
calendarTabControl.add(winterTab, text="Winter")
calendarTabControl.pack(expand=1, fill="both")

calendarFrame.pack()
for tab in [springTab, summerTab, fallTab, winterTab]:
    createBlankCalendar(tab)

root.mainloop() #Execute loop