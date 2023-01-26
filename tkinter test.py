import tkinter as tkinter
window = tkinter.Tk()
for x in range(5):
    for y in range(7):
        framegrid = tkinter.Frame(master=window, relief=tkinter.SUNKEN, borderwidth=1.5)
        framegrid.grid(row=x, column=y, padx=5, pady=5)
        labelgrid = tkinter.Label(master=framegrid, text=f"Row no. {x}\nColumn no. {y}").pack(padx=3, pady=3)
window.mainloop()