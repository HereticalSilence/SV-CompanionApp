basePrice = 1.5
userAge = ""
while userAge.lower() != "quit":
    userAge = input("Enter an age: ")
    if int(userAge) >= 16:
        basePrice = 2.50
    print ("The ticket price is £"+str(basePrice)+"0")