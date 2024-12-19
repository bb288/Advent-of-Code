# Data inlezen
data_bestand = open("2024\\12 december\\Data\\Input_12122024.txt", 'r')
#data_bestand = open("2024\\12 december\\Data\\Input_12122024_test.txt", 'r')
data_1 = data_bestand.read().split()

data = []
for line in data_1:
    listArray = []
    for point in list(line):
        listArray.append(point)
    data.append(listArray)

width = len(data[0])
heigth = len(data)

def findAreaPerimeter(x, y, doneCoor, value):
    if [x, y] in doneCoor:
        return 0, 0, doneCoor
    area = 1
    perimeter = 0
    doneCoor.append([x, y])
    #Check top
    if y - 1 < 0:
        perimeter += 1
    elif value == data[y-1][x]:
        if not([x, y-1] in doneCoor):
            returnValue = findAreaPerimeter(x, y-1, doneCoor, value)
            area += returnValue[0]
            perimeter += returnValue[1]
            doneCoor = returnValue[2]
    else:
        perimeter += 1

    #Check right
    if x + 1 > width - 1:
        perimeter += 1
    elif value == data[y][x+1]:
        if not([x+1, y] in doneCoor):
            returnValue = findAreaPerimeter(x+1, y, doneCoor, value)
            area += returnValue[0]
            perimeter += returnValue[1]
            doneCoor = returnValue[2]
    else:
        perimeter += 1

    #Check bottom
    if y + 1 >= heigth:
        perimeter += 1
    elif value == data[y+1][x]:
        if not([x, y+1] in doneCoor):
            returnValue = findAreaPerimeter(x, y+1, doneCoor, value)
            area += returnValue[0]
            perimeter += returnValue[1]
            doneCoor = returnValue[2]
    else:
        perimeter += 1

    #Check left
    if x - 1 < 0:
        perimeter += 1
    elif value == data[y][x-1]:
        if not([x-1, y] in doneCoor):
            returnValue = findAreaPerimeter(x-1, y, doneCoor, value)
            area += returnValue[0]
            perimeter += returnValue[1]
            doneCoor = returnValue[2]
    else:
        perimeter += 1

    return area, perimeter, doneCoor

doneCoor = []
totalCost = 0
y = 0
while y < len(data):
    x = 0
    while x < len(data[y]):
        if not([x, y] in doneCoor):
            returnValue = findAreaPerimeter(x, y, doneCoor, data[y][x])
            doneCoor = returnValue[2]
            totalCost += returnValue[0] * returnValue[1]
        x += 1
    y += 1



print(totalCost)
