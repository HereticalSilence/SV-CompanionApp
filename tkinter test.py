import tkinter as tkinter
window = tkinter.Tk()
for x in range(4):
    for y in range(2):
        framegrid = tkinter.Frame(
        master=window,
        relief=tkinter.SUNKEN,
        borderwidth=1.5
        )
        framegrid.grid(row=x, column=y, padx=5, pady=5)
        labelgrid = tkinter.Label(master=framegrid, text=f"Row no. {x}\nColumn no. {y}")
        labelgrid.pack(padx=3, pady=3)
        window.mainloop()