# Data inlezen
data_bestand = open("2024\\11 december\\Data\\Input_11122024.txt", 'r')
#data_bestand = open("2024\\11 december\\Data\\Input_11122024_test.txt", 'r')
data = data_bestand.read().split()

#print(data)

def blink(numberOfBlinks, number):
    if numberOfBlinks >= 25:
        return 1
    lengthNumber = len(str(number))

    if number == 0:
        rocks = blink(numberOfBlinks + 1, 1)
    elif lengthNumber % 2 == 0:
        middle = int(lengthNumber / 2)
        leftRock = int(str(number)[0:middle])
        rightRock = int(str(number)[middle:])
        rocks = blink(numberOfBlinks + 1, leftRock) 
        rocks += blink(numberOfBlinks + 1, rightRock) 
    else:
        rocks = blink(numberOfBlinks + 1, number * 2024)
    return rocks

numberOfRocks = 0
for stone in data:
    print(stone)
    numberOfRocks += blink(0, int(stone))

print(numberOfRocks)