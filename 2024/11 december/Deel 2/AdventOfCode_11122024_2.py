from datetime import datetime
# Data inlezen
data_bestand = open("2024\\11 december\\Data\\Input_11122024.txt", 'r')
#data_bestand = open("2024\\11 december\\Data\\Input_11122024_test.txt", 'r')
data = data_bestand.read().split()

pastStones = dict()
pastStones[-1,-1] = -1

def blink(numberOfBlinks, number):
    rocks = 1    
    if numberOfBlinks >= 75:
        return 1
    lengthNumber = len(str(number))

    if (numberOfBlinks, number) in pastStones.keys():
        rocks = pastStones[numberOfBlinks, number]
    elif number == 0:
        rocks = blink(numberOfBlinks + 1, 1)
    elif lengthNumber % 2 == 0:
        middle = int(lengthNumber / 2)
        leftRock = int(str(number)[0:middle])
        rightRock = int(str(number)[middle:])
        rocks = blink(numberOfBlinks + 1, leftRock) 
        rocks += blink(numberOfBlinks + 1, rightRock) 
    else:
        rocks = blink(numberOfBlinks + 1, number * 2024)
    if not((numberOfBlinks, number) in pastStones.keys()):
        pastStones[numberOfBlinks, number] = rocks

    return rocks

totalNumberOfRocks = 0
for stone in data:
    numberOfRocks = blink(0, int(stone))
    print("End time: " + str(datetime.now().time()))

print(totalNumberOfRocks)