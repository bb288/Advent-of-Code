#data_bestand = open("10 december/Data/Input_20231210.txt")
data_bestand = open("10 december/Data/Input_test.txt")
data = data_bestand.read().split('\n') # Use split on \n instead of readlines(). This makes th \n dissapear 
#print(data)

# (North, east, south, west)
movements = {"|": (1, 0, 1, 0), "-": (0, 1, 0, 1), "L": (1, 1, 0, 0), "J": (1, 0, 0, 1), "7": (0, 0, 1, 1), "F": (0, 1, 1, 0), ".": (0, 0, 0, 0)}
directions = ["N", "E", "S", "W"]
map = []
i = 0
j = 0
lengthPipe = 0

for line in data:
    map.append(line.strip())

# Find start point:
for i in range(len(map)):
    for j in range(len(map[i])):
        if map[i][j] == 'S':
            startPoint = (i, j)

#print(map)
#print(startPoint)

def nextPoint(currentPoint, nextDir):
    if nextDir == "N":
        nextPoint = (currentPoint[0] - 1, currentPoint[1])
    elif nextDir == "E":
        nextPoint = (currentPoint[0], currentPoint[1] + 1)
    elif nextDir == "S":
        nextPoint = (currentPoint[0] + 1, currentPoint[1])
    elif nextDir == "W":
        nextPoint = (currentPoint[0], currentPoint[1] - 1)
    return nextPoint

def nextDirection(nextPoint, prevDir):
    movement = movements[map[nextPoint[0]][nextPoint[1]]]
    if movement[0] == 1 and prevDir != "N":
        return "N"
    elif movement[1] == 1 and prevDir != "E":
        return "E"
    elif movement[2] == 1 and prevDir != "S":
        return "S"
    elif movement[3] == 1 and prevDir != "W":
        return "W"

def oppositeDirection(direction):
    if direction == "N":
        return "S"
    elif direction == "E":
        return "W"
    elif direction == "S":
        return "N"
    elif direction == "W":
        return "E"
    
# Find S directions
def validDirection(currentPoint, nextDir, prevDir):
    checkPoint = nextPoint(currentPoint, nextDir)

    if not(checkPoint[0] >= 0 and checkPoint[1] >= 0):
        return False
    
    if map[checkPoint[0]][checkPoint[1]] == "S":
        return True
    
    movement = movements[map[checkPoint[0]][checkPoint[1]]]

    if prevDir == "N" and movement[0] == 1:
        return True
    elif prevDir == "E" and movement[1] == 1:
        return True
    elif prevDir == "S" and movement[2] == 1:
        return True
    elif prevDir == "W" and movement[3] == 1:
        return True
    else:
        return False

highLengthLoop = 0
highPath = []

for direction in directions:
    sContinue = 1
    totalLengthLoop = 0
    path = []

    currentPoint = startPoint
    nextDir = direction # Direction point is going to
    prevDir = oppositeDirection(nextDir)

    while sContinue == 1:
        if not(validDirection(currentPoint, nextDir, prevDir)):
            sContinue == 0
            break

        totalLengthLoop += 1
        path.append(currentPoint)
#        print(path)

        currentPoint = nextPoint(currentPoint, nextDir)

        if currentPoint == startPoint and totalLengthLoop > 0:
            sContinue == 0
            break

        nextDir = nextDirection(currentPoint, prevDir)
        prevDir = oppositeDirection(nextDir)
    
    if totalLengthLoop > highLengthLoop:
        highLengthLoop = totalLengthLoop
        highPath = path

#    print(totalLengthLoop)
#    print(highLengthLoop)

print("Answer = " + str(round(highLengthLoop / 2)))
print(highPath)