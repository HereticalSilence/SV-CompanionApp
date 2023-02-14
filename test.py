testList = [13, 14]

def myFunc(list):
    list[0] += 1
    list[1] += 1
    return list

print (testList, myFunc(testList), testList)