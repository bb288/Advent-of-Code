# Data inlezen
data_bestand = open("2024\\11 december\\Data\\Input_11122024.txt", 'r')
#data_bestand = open("2024\\11 december\\Data\\Input_11122024_test.txt", 'r')
data = data_bestand.read().split()

print(data)

def blink(numberOfBlinks, number):
    if numberOfBlinks >= 25:
        return 1
#    print("start Rock: " + str(number) + " en blinks = " + str(numberOfBlinks))
    lengthNumber = len(str(number))

    if number == 0:
#        print(1)
        rocks = blink(numberOfBlinks + 1, 1)
    elif lengthNumber % 2 == 0:
        middle = int(lengthNumber / 2)
        leftRock = int(str(number)[0:middle])
#        print(leftRock)
        rightRock = int(str(number)[middle:])
#        print(rightRock)
        rocks = blink(numberOfBlinks + 1, leftRock) 
        rocks += blink(numberOfBlinks + 1, rightRock) 
    else:
#        print(number * 2024)
        rocks = blink(numberOfBlinks + 1, number * 2024)
    return rocks

numberOfRocks = 0
for stone in data:
    print(stone)
    numberOfRocks += blink(0, int(stone))

print(numberOfRocks)

#print(blink(0, 125))

#print(numberOfRocks)