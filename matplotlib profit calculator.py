import matplotlib.pyplot as plt
import numpy as np
import math

plt.style.use('_mpl-gallery')

def calculatePickleValue(baseValue: int):
    return math.trunc(2 * baseValue + 50)

def calculateWineValue(baseValue: int):
    return math.trunc(3* baseValue)

def calculateJuiceValue(baseValue: int):
    return math.trunc(2.25 * baseValue)

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
        "14": [0, 0, 0.46, 0.55]
        }
}

#Cost per seed, base value, base jelly, base wine, grow time, regrow time, extra produce, chance of extra produce
cropDictionary = {
    "Spring": {
        "Blue Jazz": [30, 50, 0, 0, 7, 0, 0, 0],
        "Cauliflower": [80, 175, calculatePickleValue(175), calculateJuiceValue(175), 12, 0, 0, 0],
        "Coffee Bean": [2500, 15, 0, calculatePickleValue(15), 10, 2, 3, 1],
        "Garlic": [40, 60, calculatePickleValue(60), calculateJuiceValue(60), 4, 0, 0, 0],
        "Green Bean": [60, 40, calculatePickleValue(40), calculateJuiceValue(40), 10, 3, 0, 0],
        "Kale": [70, 110, calculatePickleValue(110), calculateJuiceValue(110), 6, 0, 0, 0],
        "Parsnip": [20, 35, calculatePickleValue(35), calculateJuiceValue(35), 4, 0, 0, 0],
        "Potato": [50, 80, calculatePickleValue(80), calculateJuiceValue(80), 6, 0, 1, 0.25],
        "Rhubarb": [100, 220, calculatePickleValue(220), calculateJuiceValue(220), 13, 0, 0, 0],
        "Strawberry": [100, 120, calculatePickleValue(120), calculateWineValue(120), 8, 4, 1, 0.02],
        "Tulip": [25, 30, 0, 0, 6, 0, 0, 0],
        "Unmilled Rice": [40, 30, calculatePickleValue(30), calculateJuiceValue(30), 8, 0, 1, 0.11],
        }
    }

def sortKeyFunction(e):
    return e[1]
"""
farmingLevel = int(input("What level farming are you?\n"))
tillerCheck = input("Do you have the tiller skill | Y/N\n")
artisanCheck = input("Do you have the artisan skill | Y/N\n")
seedMoney = int(input("How much g do you have for seeds\n"))
fertiliserInput = int(input("Fertiliser | 0 | 1 | 2 | 3 |\n"))
userInput = input("Spring crops: Raw, Jar, Keg\n")
"""

def generatePlot(farmingLevel,tillerCheck,artisanCheck,seedMoney,fertiliserInput,userInput, day):
    cropList = []
    cropValues = []

    if tillerCheck.lower() == "y":
        tillerBonus = 1.1

    if artisanCheck.lower() == "y":
        artisanBonus = 1.4

    if fertiliserInput == 0:
        harvestRatio = cropQuality["None"][str(farmingLevel)]
    elif fertiliserInput == 1:
        harvestRatio = cropQuality["Basic Fertilizer"][str(farmingLevel)]
    elif fertiliserInput == 2:
        harvestRatio = cropQuality["Quality Fertilizer"][str(farmingLevel)]
    elif fertiliserInput == 3:
        harvestRatio = cropQuality["Deluxe Fertilizer"][str(farmingLevel)]

    if userInput.lower() == "raw":
        #do the rawr
        for x, y in cropDictionary["Spring"].items():
            seedAmount = seedMoney // y[0]
            profitFromRaw = 0
            print (x, harvestRatio)
            cropQualityMultiplier = 1
            #Extra regrows
            if y[5] != 0:
                dayOfRegrowthStart = day + y[4]
                numHarvests = (28 - dayOfRegrowthStart) // y[5]
            if y[5] == 0:
                numHarvests = (28-day) // y[4]
            for qualityLevel in harvestRatio:
                print (math.trunc(seedAmount * y[1] * qualityLevel * cropQualityMultiplier  * tillerBonus))
                profitFromRaw += (seedAmount * y[1] * qualityLevel * cropQualityMultiplier * tillerBonus)
                cropQualityMultiplier += 0.25

            cropList.append([x + "\n" + str(seedAmount) + "\n" + str(numHarvests) + " harvests", math.trunc(profitFromRaw-(seedMoney))])    
            
    elif userInput.lower() == "jar":
        #my dick in a jar
        pass
    elif userInput.lower() == "keg":
        #PEG ME MOMMY
        pass

    cropList.sort(reverse=True, key=sortKeyFunction)
    cropNames = []
    cropValues = []

    for crop in cropList:
        cropNames.append(crop[0])
        cropValues.append(crop[1])

    # make data:
    crops = cropNames
    values = cropValues

    plt.bar(crops,values)
    plt.title(f'Spring Crops with {seedMoney}g')
    plt.xlabel("Crops")
    plt.ylabel("Profit")
generatePlot(10,"y","y",5000,0,"raw", 1)
#generatePlot(10,"y","y",5000,3,"raw", 5)
plt.show()