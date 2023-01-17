
#!/usr/bin/env python
import PySimpleGUI as sg
import random
import string

"""
    Basic use of the Table Element
    
    Copyright 2022 PySimpleGUI
"""


# ------ Some functions to help generate data for the table ------
def word():
    return ''.join(random.choice(string.ascii_lowercase) for i in range(10))
def number(max_val=1000):
    return random.randint(0, max_val)

def make_table(num_rows, num_cols):
    dates = []
    start = 1
    for x in range(num_rows):
        week = []
        for y in range(num_cols):
            week.append(start)
            start += 1
        dates.append(week)
    return dates

        

# ------ Make the Table Data ------
data = make_table(num_rows=4, num_cols=7)
headings = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# ------ Window Layout ------
layout = [[sg.Table(values=data, headings=headings, max_col_width=25,
                    auto_size_columns=False,
                    # cols_justification=('left','center','right','c', 'l', 'bad'),       # Added on GitHub only as of June 2022
                    display_row_numbers=False,
                    justification='center',
                    num_rows=4,
                    row_height=50,
                    key='-TABLE-',
                    enable_events=True,
                    expand_x=False,
                    expand_y=False,
                    vertical_scroll_only=False,
                    enable_click_events=True)]]

# ------ Create Window ------
window = sg.Window('The Table Element', layout,
                   # ttk_theme='clam',
                   # font='Helvetica 25',
                   resizable=True
                   )

# ------ Event Loop ------
while True:
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED:
        break


