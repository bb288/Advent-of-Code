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
dir = 0
y = currentLocation[1]
x = currentLocation[0]
map[y][x] = 'X'
totalSpaces = 1

while not(y + directions[dir][1] < 0 or y + directions[dir][1] > len(map) - 1 or x + directions[dir][0] < 0 or x + directions[dir][0] > len(map[0]) - 1):
    nextPoint = map[y + directions[dir][1]][x + directions[dir][0]]
    if nextPoint == '#':
        if dir == len(directions) - 1:
            dir = 0
        else:
            dir += 1
    else:
        if not(nextPoint == 'X'):
            totalSpaces += 1
            map[y + directions[dir][1]][x + directions[dir][0]] = 'X'
        currentLocation = [x + directions[dir][0], y + directions[dir][1]]
        y = currentLocation[1]
        x = currentLocation[0]

print(totalSpaces)