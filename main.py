import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

class Main(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Stardew Valley Companion App')
        self.geometry('1280x720')

        self.label = ttk.Label(self, text='Stardew Valley Companion').pack()
        self.button = ttk.Button(self, text='Click me')
        self.button['command'] = self.button_clicked
        self.button.pack()
    
    

    def button_clicked(self):
        showinfo(title='Stardew Valley Companion', message='Stardew Valley Companion Message')

if __name__ == "__main__":
    app = Main()
    app.mainloop()