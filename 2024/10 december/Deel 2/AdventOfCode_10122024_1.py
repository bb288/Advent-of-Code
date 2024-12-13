# Data inlezen
data_bestand = open("2024\\10 december\\Data\\Input_10122024.txt", 'r')
#data_bestand = open("2024\\10 december\\Data\\Input_10122024_test.txt", 'r')
data_1 = data_bestand.read().split()

data = []
for line in data_1:
    intList = []
    for point in list(line):
        intList.append(int(point))
    data.append(intList)

width = len(data[0])
heigth = len(data)
def searchNextStep(currentNumber, currentX, currentY):
    ends = 0
    if currentNumber == 9:
        return 1
    #searchRight
    if currentX + 1 < width:
        if data[currentY][currentX + 1] == currentNumber + 1:
            ends += searchNextStep(currentNumber + 1, currentX + 1, currentY)
    #searchBelow
    if currentY + 1 < heigth:
        if data[currentY + 1][currentX] == currentNumber + 1:
            ends += searchNextStep(currentNumber + 1, currentX, currentY + 1)
    #SearchLeft
    if currentX - 1 >= 0:
        if data[currentY][currentX - 1] == currentNumber + 1:
            ends += searchNextStep(currentNumber + 1, currentX - 1, currentY)
    #searchTop
    if currentY - 1 >= 0:
        if data[currentY - 1][currentX] == currentNumber + 1:
            ends += searchNextStep(currentNumber + 1, currentX, currentY - 1)
    return ends

totalEnds = 0
for y in range(0, len(data)):
    for x in range(0, len(data[y])):
        if data[y][x] == 0:
            ends = searchNextStep(0, x, y, )
            totalEnds += ends
            print("Coördinate X=" + str(x) + ", Y=" + str(y)) 
            print("number of ends: " + str(ends))
print(totalEnds)        