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

#-=-Imports-=-#
#Tkinter related imports
from tkinter import * 
import tkinter as tkinter
from tkinter import ttk


#-=-Global Variables-=-#
#Define week days and seasons list
weekList = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
seasons = ["Spring", "Summer", "Fall", "Winter"]

#-=-Year List-=-#
yearList = []
yearDataList =[]

#-=-Functions-=-#
#Generate a new year's worth of events to display in subsequent years on the crop planner as a nested dictionary
def generateNewYearEvents():
    data = {
        "Spring": {
            "1": [""],
            "2": [""],
            "3": [""],
            "4": ["Kent's Birthday", "PicOfKent"],
            "5": [""],
            "6": [""],
            "7": ["Lewis' Birthday", "PicOfLewis"],
            "8": [""],
            "9": [""],
            "10": ["Vincent's Birthday", "PicOfVincent"],
            "11": [""],
            "12": [""],
            "13": ["Egg Festival", "WavingFlag.gif"],
            "14": ["Haley's Birthday", "PicOfHaley"],
            "15": [""],
            "16": [""],
            "17": [""],
            "18": ["Pam's Birthday", "PicOfPam"],
            "19": [""],
            "20": ["Shane's Birthday", "PicOfShane"],
            "21": [""],
            "22": [""],
            "23": [""],
            "24": ["Flower Dance", "WavingFlag.gif"],
            "25": [""],
            "26": ["Pierre's Birthday", "PicOfPierre"],
            "27": ["Emily's Birthday", "PicOfEmily"],
            "28": [""],
        },
        "Summer": {
            "1": [""],
            "2": [""],
            "3": [""],
            "4": ["Jas' Birthday", "PicOfJas"],
            "5": [""],
            "6": [""],
            "7": [""],
            "8": ["Gus' Birthday", "PicOf"],
            "9": [""],
            "10": ["Maru's Birthday", "PicOf"],
            "11": ["Luau", "WavingFlag.gif"],
            "12": [""],
            "13": ["Alex's Birthday", "PicOf"],
            "14": [""],
            "15": [""],
            "16": [""],
            "17": ["Sam's Birthday", "PicOf"],
            "18": [""],
            "19": ["Demetrius' Birthday", "PicOf"],
            "20": [""],
            "21": [""],
            "22": ["Dwarf's Birthday", "PicOf"],
            "23": [""],
            "24": ["Willy's Birthday", "PicOf"],
            "25": [""],
            "26": ["Leo's Birthday", "PicOf"],
            "27": [""],
            "28": ["Dance of the Moonlight Jellies", "WavingFlag.gif"]
        },
        "Fall": {
            "1": [""],
            "2": ["Penny's Birthday", "PicOf"],
            "3": [""],
            "4": [""],
            "5": ["Elliott's Birthday", "PicOf"],
            "6": [""],
            "7": [""],
            "8": [""],
            "9": [""],
            "10": [""],
            "11": ["Jodi's Birthday", "PicOf"],
            "12": [""],
            "13": ["", "PicOf"],
            "14": [""],
            "15": ["", "PicOf"],
            "16": ["", "PicOf"],
            "17": [""],
            "18": ["", "PicOf"],
            "19": [""],
            "20": [""],
            "21": ["", "PicOf"],
            "22": [""],
            "23": [""],
            "24": ["", "PicOf"],
            "25": [""],
            "26": [""],
            "27": ["", "PicOf"],
            "28": [""],
        },
        "Winter": {
            "1": [""],
            "2": [""],
            "3": [""],
            "4": [""],
            "5": [""],
            "6": [""],
            "7": [""],
            "8": [""],
            "9": [""],
            "10": [""],
            "11": [""],
            "12": [""],
            "13": [""],
            "14": [""],
            "15": [""],
            "16": [""],
            "17": [""],
            "18": [""],
            "19": [""],
            "20": [""],
            "21": [""],
            "22": [""],
            "23": [""],
            "24": [""],
            "25": [""],
            "26": [""],
            "27": [""],
            "28": [""],

        }
    }
    return data

#Create a tkinter calendar with data for a tab
def createBlankCalendar(tabToCreateAt, season):
    dayCounter = 0
    mainFrame = ttk.Frame(master=tabToCreateAt)
    for x in range(7):
        #for y in range(5):
        frameGrid = ttk.Frame(master=mainFrame, relief=tkinter.RAISED, borderwidth=2, width=125, height=25)
        frameGrid.pack_propagate(False)
        frameGrid.grid(row=1, column=x)
        labelGrid = ttk.Label(master=frameGrid, text=weekList[x]).pack()
    for y in range(2, 6):
        for x in range(7):
            dayCounter += 1
            frameGrid = ttk.Frame(master=mainFrame, relief=tkinter.RAISED, borderwidth=2, width=125, height=125)
            frameGrid.pack_propagate(False)
            frameGrid.grid(row=y, column=x)
            #print (yearDataList[len(yearDataList)-1][season].get(str(dayCounter)))
            textForGrid = str(dayCounter) + ": " + str(yearDataList[len(yearDataList)-1][season].get(str(dayCounter))[0])
            labelGrid = ttk.Label(master=frameGrid, text=textForGrid, font=("Arial", 9), justify='left').pack()
        mainFrame.pack()

#Generate a set of tabs for Spring, Summer, Fall and Winter
def tabGenerate(root):
    
    #Calendar Code
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
    yearDataList.append(generateNewYearEvents())
    tabList = [springTab, summerTab, fallTab, winterTab]
    
    for i in range(4):
        createBlankCalendar(tabList[i], seasons[i])
    return calendarFrame




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

calendar = tabGenerate(root)
#-=-UNDER MAINTENANCE-=-#
"""
yearList.append([tabGenerate(root, "Test Text 1"), "generateNewYearEvents()"])

#-=-Year List Traversal-=-#
currentPos = 0

def traverseYearListLeft():
    global currentPos
    print ("Current Year Stack Pos: " + str(currentPos) + " | " + str(yearList))
    if currentPos > 0:
        yearList[currentPos][0].after(5, yearList[currentPos][0].destroy)
        currentPos -= 1
        print ("Current Year Stack Pos: " + str(currentPos) + " | " + str(yearList))
        return currentPos, yearList[currentPos]


    
def traverseYearListRight():
    global currentPos
    print ("Current Year Stack Pos: " + str(currentPos) + " | " + str(yearList))
    currentPos += 1
    if currentPos > (len(yearList)-1):
        yearList.append([tabGenerate(root, "Text Test 2"), "generateNewYearEvents()"]) 
    yearList[currentPos-1][0].after(5, yearList[currentPos-1][0].destroy)
    print ("Current Year Stack Pos: " + str(currentPos) + " | " + str(yearList))
    return currentPos, yearList[currentPos]

"""
#-=-Year List Traversal-=-#
currentPos = 0

def traverseYearListLeft():
    global currentPos
    #print ("Current Year Stack Pos: " + str(currentPos) + " | " + str(yearDataList))
    if currentPos > 0:
        print (yearDataList[currentPos-1])

    
    

leftButton = ttk.Button(master=root, text="<---", command=lambda: traverseYearListLeft()).pack()
#rightButton = ttk.Button(master=root, text="--->", command=lambda: traverseYearListRight()).pack()

root.mainloop() #Execute loop