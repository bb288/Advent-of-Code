# Data inlezen
#data_bestand = open("2023\\11 december\\Data\\Input_11122023_test.txt", 'r')
data_bestand = open("2023\\11 december\\Data\\Input_11122023.txt", 'r')
data = data_bestand.read().split()

width = len(data[0])
allPoints = ""
i = 0
while i < width:
    allPoints += "."
    i += 1

# Check if all characters in a string are .'s
def checkAllPoints(line):
    for coordinate in line:
        if coordinate != ".":
             return False
    return True

# Add a column of points to columnIndex
def addColumnPoints(columnIndex):
    rowIndex = 0
    while rowIndex < len(data):
        data[rowIndex] = data[rowIndex][:columnIndex] + "." + data[rowIndex][columnIndex:]
        rowIndex += 1

# calculates the distance between two coordinates
def calculateDistanceCoor(coorX1, coorY1, coorX2, coorY2):
    return abs(coorX1 - coorX2) + abs(coorY1 - coorY2)

# Check all rows and add an extra row if there are only .'s in the row
rowIndex = 0
while rowIndex < len(data):
    line = data[rowIndex]
    if checkAllPoints(line):
        data.insert(rowIndex + 1, allPoints)
        rowIndex += 2
    else:
        rowIndex += 1

# Check alle columns and add an extra column if there are only .'s in the column
rowIndex = 0
columnIndex = 0
while columnIndex < len(data[0]):
    column = ""
    for line in data:
        column += line[columnIndex]
    if checkAllPoints(column):
        addColumnPoints(columnIndex)
        columnIndex += 2
    else:
        columnIndex += 1

# Make a dictionary of all #'s (planets) and there coordinates
planets = {}

rowIndex = 0
planetCount = 1
for rowIndex in range(len(data)):
    columnIndex = 0
    for columnIndex in range(len(data[0])):
        if data[rowIndex][columnIndex] == "#":
            planets[planetCount] = [rowIndex, columnIndex]
            planetCount += 1

totalDistance = 0
# For each planet search the 
for planetFrom in planets:
    for planetTo in planets:
        totalDistance += calculateDistanceCoor(planets[planetFrom][0], planets[planetFrom][1], planets[planetTo][0], planets[planetTo][1])

totalDistance /= 2

print(totalDistance)




#print(data_1)