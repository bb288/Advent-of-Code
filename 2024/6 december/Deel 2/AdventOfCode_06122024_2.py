import copy

# Data inlezen
data_bestand = open("2024\\6 december\\Data\\Input_06122024.txt", 'r')
#data_bestand = open("2024\\6 december\\Data\\Input_06122024_test.txt", 'r')
data = data_bestand.read().split()

map = []
for line in data:
    map.append(list(line))

x = 0
y = 0
for line in data:
    x = 0
    for point in line:
        if point == "^":
            currentLocation = [x,y]
            break
        x += 1
    y += 1

directions = [[0, -1], [1, 0], [0, 1], [-1, 0]]
y = currentLocation[1]
x = currentLocation[0]
map[y][x] = []
map[y][x].append(0)

def turn(dir):
    if dir == len(directions) - 1:
        return 0
    else:
        return dir + 1

def sameDirection(values, dir):
    for value in values:
        if value == dir:
            return True
    return False 

def checkLoop(map, currentLocation):
    mapFunc = copy.deepcopy(map)
    dir = 0
    y = currentLocation[1]
    x = currentLocation[0]
    while not(y + directions[dir][1] < 0 or y + directions[dir][1] > len(mapFunc) - 1 or x + directions[dir][0] < 0 or x + directions[dir][0] > len(mapFunc[0]) - 1):
#        print(currentLocation)
        nextPoint = mapFunc[y + directions[dir][1]][x + directions[dir][0]]
        if nextPoint == '#':
            dir = turn(dir)
        elif not(nextPoint == '.'):
#            print("Next Point = " + str(nextPoint))
#            print("Direction = " + str(dir))
            if sameDirection(nextPoint, dir):
#                print(mapFunc)
#                print(currentLocation)
                return True
            else:
                mapFunc[y + directions[dir][1]][x + directions[dir][0]].append(dir)
                currentLocation = [x + directions[dir][0], y + directions[dir][1]]
        else:
            mapFunc[y + directions[dir][1]][x + directions[dir][0]] = []
            mapFunc[y + directions[dir][1]][x + directions[dir][0]].append(dir)
            currentLocation = [x + directions[dir][0], y + directions[dir][1]]
        y = currentLocation[1]
        x = currentLocation[0]
    return False

#map[9][9] = '#'
#print(checkLoop(map, currentLocation))
#"""
nLoops = 0
y = 0
while y < len(map):
    x = 0
    while x < len(map[0]):
        oldValue = map[y][x]
        map[y][x] = '#'
#        print(map)
#        print(currentLocation)
        if checkLoop(map, currentLocation):
            print("Loop op x = " + str(x) + " en y = " + str(y))
            nLoops += 1
        map[y][x] = oldValue
        x += 1
    y += 1
print(nLoops)
#"""

#print(map)
#print(nSteps)
#print(nLoops)