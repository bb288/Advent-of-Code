#data_bestand = open("2023/10 december/Data/Input_20231210.txt")
data_bestand = open("10 december/Data/Input_test.txt")
data = data_bestand.read().split('\n') # Use split on \n instead of readlines(). This makes th \n dissapear 
print(data)

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
            print(map[i][j])
            break

print(map)
print(startPoint)

# Find S directions








def validDirection(currentPoint):
    

    return True



for direction in directions:
    currentPoint = startPoint
    sContinue = 1
    nextDir = direction # Where to
#    if direction == "N":
#        prevDir = "S"
#    elif direction == "E":
#        prevDir = "W"
#    elif direction == "S":
#        prevDir = "N"
#    elif direction == "W":
#        prevDir = "W"

    while sContinue == 1:
        # Check if the next direction is posible
        if not(validDirection(currentPoint)):
            sContinue = 0
            break




#        nextPoint = 

#        to = 




