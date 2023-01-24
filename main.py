import PySimpleGUI as sg
import sqlite3
import math
sg.theme('DarkTeal2')
#sg.theme('Material2')
#Fetch Crop files from database for Spring
connection = sqlite3.connect('SVPCC.db')
cursor = connection.cursor()
result = cursor.execute('''SELECT * FROM SpringCrops''')
fetchAll = result.fetchall()
springCrops = {}
for item in fetchAll:
    springCrops[item[1]] = item
springCropsNames = []
for crop in springCrops:
    springCropsNames.append(crop)
  
def make_table(num_rows, num_cols):
    dates = []
    start = 1
    for x in range(num_rows):
        week = []
        for y in range(num_cols):
            week.append(str(start))
            start += 1
        dates.append(week)
    return dates

# ------ Make the Table Data ------
yearData = []
for x in range(4):
    data = make_table(num_rows=4, num_cols=7)
    yearData.append(data)
headings = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# ------ Window Layout ------
CalendarBase_layout = []
for x in range(4):
    CalendarBase_layout.append([[sg.Table(values=yearData[x], headings=headings, max_col_width=50,
                    auto_size_columns=False,
                    # cols_justification=('left','center','right','c', 'l', 'bad'),       # Added on GitHub only as of June 2022
                    display_row_numbers=False,
                    justification='left',
                    num_rows=4,
                    row_height=100,
                    key='Season'+str(x),
                    enable_events=False,
                    expand_x=True,
                    expand_y=True,
                    hide_vertical_scroll=True,
                    enable_click_events=True)]])


userInfo_layout =  [[sg.Text("Farming Level", justification='center'), sg.Input(default_text="0", key="FarmLevel", justification='center', enable_events=True)],  
                [sg.Text("Level 5 Professions:"), sg.Checkbox("Tiller", key='TillerSkill', disabled=True, pad=(0,0), enable_events=True, tooltip="Crops worth 10% more")], 
                [sg.Text("Level 10 Professions"), sg.Checkbox("Agriculturist", key='AgriculturistSkill', disabled=True, pad=(0,0), enable_events=True, tooltip="All crops grow 10% faster"), sg.Checkbox("Artisan", key='ArtisanSkill', disabled=True, pad=(0,0), enable_events=True, tooltip="Artisan goods worth 40% more")], [sg.Button("OK")]] 


cropQuality = {
    'None' : {
        "0": [0.97, 0.02, 0.01],
        "1": [0.91, 0.06, 0.03],
        "2": [0.85, 0.1, 0.05],
        "3": [0.8, 0.13, 0.07],
        "4": [0.75, 0.16, 0.09],
        "5": [0.69, 0.2, 0.11],
        "6": [0.64, 0.23, 0.13],
        "7": [0.60, 0.25, 0.15],
        "8": [0.55, 0.28, 0.17],
        "9": [0.50, 0.31, 0.19],
        "10": [0.46, 0.33, 0.21],
        "11": [0.42, 0.35, 0.23],
        "12": [0.38, 0.37, 0.25],
        "13": [0.34, 0.39, 0.27],
        "14": [0.30, 0.41, 0.29]
    },
    
    "Basic Fertilizer" : {
        "0": [0.88, 0.08, 0.04],
        "1": [0.77, 0.15, 0.08],
        "2": [0.68, 0.20, 0.12],
        "3": [0.59, 0.26, 0.15],
        "4": [0.50, 0.31, 0.19],
        "5": [0.42, 0.35, 0.23],
        "6": [0.35, 0.39, 0.26],
        "7": [0.28, 0.42, 0.30],
        "8": [0.22, 0.44, 0.34],
        "9": [0.16, 0.47, 0.37],
        "10": [0.15, 0.44, 0.41],
        "11": [0.14, 0.41, 0.45],
        "12": [0.13, 0.39, 0.48],
        "13": [0.12, 0.36, 0.52],
        "14": [0.11, 0.33, 0.56]
    },

    'Quality Fertilizer' : {
        "0": [0.78, 0.14, 0.08],
        "1": [0.64, 0.23, 0.13],
        "2": [0.52, 0.30, 0.18],
        "3": [0.40, 0.36, 0.24],
        "4": [0.30, 0.41, 0.29],
        "5": [0.21, 0.45, 0.34],
        "6": [0.15, 0.45, 0.40],
        "7": [0.14, 0.41, 0.45],
        "8": [0.13, 0.37, 0.50],
        "9": [0.11, 0.33, 0.56],
        "10": [0.10, 0.29, 0.61],
        "11": [0.09, 0.25, 0.66],
        "12": [0.07, 0.21, 0.72],
        "13": [0.06, 0.17, 0.77],
        "14": [0.04, 0.13, 0.82]
        },

    'Deluxe Fertilizer' : {
        "0": [0, 0.84, 0.10, 0.06],
        "1": [0, 0.75, 0.16, 0.09],
        "2": [0, 0.66, 0.22, 0.13],
        "3": [0, 0.57, 0.27, 0.16],
        "4": [0, 0.49, 0.31, 0.20],
        "5": [0, 0.42, 0.35, 0.23],
        "6": [0, 0.35, 0.39, 0.27],
        "7": [0, 0.28, 0.42, 0.30],
        "8": [0, 0.22, 0.45, 0.34],
        "9": [0, 0.16, 0.47, 0.37],
        "10": [0, 0.11, 0.48, 0.41],
        "11": [0, 0.07, 0.49, 0.44],
        "12": [0, 0.03, 0.50, 0.47],
        "13": [0, 0, 0.49, 0.51],
        "14": [0, 0, 0.46, 0.55]
        }
}

def moneyCalculation(tableID, farmLevel, crop, amount: int, fertilizer):
    if fertilizer == "Speed-Gro" or fertilizer == "Deluxe Speed-Gro" or fertilizer == "Hyper Speed-Gro":
        fertilizer = "None"
    qualityCalcValues = cropQuality[fertilizer][str(farmLevel)]
    cropValue = springCrops[crop][6]
    cropRawQuantityCeil = []
    cropRawQuantityFloor = []
    for x in range(len(qualityCalcValues)):
        cropRawQuantityCeil.append(math.ceil(float(amount) * qualityCalcValues[x]))
        cropRawQuantityFloor.append(math.floor(float(amount) * qualityCalcValues[x]))
    yearData[0][tablePos[0]][tablePos[1]] += "\n"+crop + " x" + str(amount)
    window[tableID].update(values=yearData[0])


def createPlantWindow():
    return [[sg.Text("Crops"), 
    sg.Combo(values=springCropsNames, default_value="Please select a crop", readonly=True, size=(20, 5), key='springCropSelector', enable_events=True), 
    sg.Text("Quantity"), 
    sg.In(key="QuantityIn", size=(10,5)), 
    sg.Text("Fertilizer"),
    sg.Combo(values=["Basic Fertilizer", "Quality Fertilizer", "Deluxe Fertilizer", "Speed-Gro", "Deluxe Speed-Gro", "Hyper Speed-Gro"], default_value="None", readonly=True, size=(20, 5), key='springFertilizer', enable_events=True), 
    sg.Button("+", font=('bold', 20), key="plantWindowButton")]]



main_layout = [[sg.Column(
            [[sg.Frame(title="Calendar", font=('bold', 15),
            layout=[[sg.TabGroup(
                [[sg.Tab('Spring', CalendarBase_layout[0], expand_x=True, expand_y=True), 
                sg.Tab('Summer', CalendarBase_layout[1], expand_x=True, expand_y=True),
                sg.Tab('Fall', CalendarBase_layout[2], expand_x=True, expand_y=True),
                sg.Tab('Winter', CalendarBase_layout[3], expand_x=True, expand_y=True)]], 
                pad=(5,5), tooltip='Calendar', size = (900, 500))]])]], justification='center'), 
                sg.Frame(title="Tooltips", expand_x=True, font=('bold', 15),
                layout=[[
                    sg.Column(justification='center',
                        layout=[[sg.Text("Base Price")], 
                        [sg.Text("(0% Bonus)", font=('italics', 8))], 
                        [sg.Image(source="Images/base_melon.png", subsample=2, tooltip="Base Quality Crops"), sg.Text("320g")],  
                        [sg.Image(source="Images/silver_melon.png", subsample=2, tooltip="Silver Quality Crops"), sg.Text("400g")], 
                        [sg.Image(source="Images/gold_melon.png", subsample=2, tooltip="Gold Quality Crops"), sg.Text("480g")], 
                        [sg.Image(source="Images/iridium_melon.png", subsample=2, tooltip="Iridium Quality Crops"), sg.Text("640g")],
                        [sg.Text(" ")], 
                        [sg.Text("Artisan Price")],
                        [sg.Text("(+40% Bonus)", font=('italics', 8))],
                        [sg.Image(source="Images/wine_melon.png", subsample=2, tooltip="Base Quality Wine"), sg.Text("1050g")],
                        [sg.Image(source="Images/wine_melon.png", subsample=2, tooltip="Silver Quality Aged Wine"), sg.Text("1311g")],
                        [sg.Image(source="Images/wine_melon.png", subsample=2, tooltip="Gold Quality Aged Crops"), sg.Text("1575g")],
                        [sg.Image(source="Images/wine_melon.png", subsample=2, tooltip="Iridium Quality Aged Crops"), sg.Text("2100g")],
                        [sg.Image(source="Images/juice_pumpkin.png", subsample=2, tooltip="Juice can't be aged"), sg.Text("1008g")],
                        [sg.Image(source="Images/pickle_pumpkin.png", subsample=2, tooltip="Pickles/Jellies can't be aged"), sg.Text("966g")]
                        ]), 
                    sg.Column(layout=[
                        [sg.Text("|", font=(20))],
                        [sg.Text("|", font=(20))],
                        [sg.Text("|", font=(20))],
                        [sg.Text("|", font=(20))],
                        [sg.Text("|", font=(20))],
                        [sg.Text("|", font=(20))],
                        [sg.Text("|", font=(20))],
                        [sg.Text("|", font=(20))],
                        [sg.Text("|", font=(20))],
                        [sg.Text("|", font=(20))],
                        [sg.Text("|", font=(20))],
                        [sg.Text("|", font=(20))]
                        ]),
                    sg.Column(
                        layout=[[sg.Text("Tiller Price")], 
                        [sg.Text("(10% Bonus)", font=('italics', 8))], 
                        [sg.Image(source="Images/base_melon.png", subsample=2, tooltip="Base Quality Crops"), sg.Text("352g")],  
                        [sg.Image(source="Images/silver_melon.png", subsample=2, tooltip="Silver Quality Crops"), sg.Text("440g")], 
                        [sg.Image(source="Images/gold_melon.png", subsample=2, tooltip="Gold Quality Crops"), sg.Text("528g")], 
                        [sg.Image(source="Images/iridium_melon.png", subsample=2, tooltip="Iridium Quality Crops"), sg.Text("704g")],
                        [sg.Text(" ")], 
                        [sg.Text("Artisan Price")],
                        [sg.Text("(+40% Bonus)", font=('italics', 8))],
                        [sg.Image(source="Images/wine_melon.png", subsample=2, tooltip="Base Quality Wine"), sg.Text("1050g")],
                        [sg.Image(source="Images/wine_melon.png", subsample=2, tooltip="Silver Quality Aged Wine"), sg.Text("1311g")],
                        [sg.Image(source="Images/wine_melon.png", subsample=2, tooltip="Gold Quality Aged Crops"), sg.Text("1575g")],
                        [sg.Image(source="Images/wine_melon.png", subsample=2, tooltip="Iridium Quality Aged Crops"), sg.Text("2100g")],
                        [sg.Image(source="Images/juice_pumpkin.png", subsample=2, tooltip="Juice can't be aged"), sg.Text("1008g")],
                        [sg.Image(source="Images/pickle_pumpkin.png", subsample=2, tooltip="Pickles/Jellies can't be aged"), sg.Text("966g")]]) 
                        ]], 
                    size=(220, 500))]], [sg.Column([[sg.Frame(title="User Information", layout=userInfo_layout)]], justification='center')]
 
window = sg.Window('SVPCC', main_layout, default_element_size=(12,1), size=(1280,720))
while True:    
    event, values = window.read()
    if type(event) is tuple:
        tablePos = event[2]
        print (tablePos)
        print (tablePos[0])
        print (tablePos[1])
        if event[0] == "Season0":
            plant = sg.Window(title='Edit Day', layout=createPlantWindow())
            while True:
                eventPlant, valuesPlant = plant.read()
                print (eventPlant)
                if eventPlant == 'plantWindowButton':
                    print (valuesPlant['springCropSelector'], valuesPlant['QuantityIn'], valuesPlant['springFertilizer'])
                    moneyCalculation('Season0', values['FarmLevel'], valuesPlant['springCropSelector'], valuesPlant['QuantityIn'], valuesPlant['springFertilizer'])
                if eventPlant == sg.WIN_CLOSED:              
                    break

    
    try:
        if int(values['FarmLevel']) < 5:
            window['TillerSkill'].update(disabled=True)
            window['AgriculturistSkill'].update(disabled=True)
            window['ArtisanSkill'].update(disabled=True)
        elif 5 <= int(values['FarmLevel']) <= 10:        
            window['TillerSkill'].update(disabled=False)

            if int(values['FarmLevel']) == 10:
                if values['AgriculturistSkill']:
                    window['ArtisanSkill'].Update(disabled=True)
                if values['AgriculturistSkill'] == False:
                    window['ArtisanSkill'].update(disabled=False)

                if values['ArtisanSkill']:
                    window['AgriculturistSkill'].Update(disabled=True)
                if values['ArtisanSkill'] == False:
                    window['AgriculturistSkill'].update(disabled=False)
        else:
            window['TillerSkill'].update(disabled=True)
            window['AgriculturistSkill'].update(disabled=True)
            window['ArtisanSkill'].update(disabled=True)
            sg.popup(title=None, custom_text="Error! Please enter a correct farming skill level")
    except:
        pass
    if event == sg.WIN_CLOSED:              
        break 
    #print (event, values)
window.close()