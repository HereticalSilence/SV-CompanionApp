from tkinter import * #Import TK

root = Tk() #Create root window

root.title("Stardew Valley Companion App") #Assign window title
root.geometry('1280x720') #Set window size 

menu = Menu(root)
item = Menu(menu)
item.add_command(label='Save')
item.add_command(label='Load')
menu.add_cascade(label='File', menu=item)
root.config(menu=menu)


root.mainloop() #Execute loop