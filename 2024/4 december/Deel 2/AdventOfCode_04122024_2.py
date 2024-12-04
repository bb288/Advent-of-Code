# Data inlezen
data_bestand = open("2024\\4 december\\Data\\Input_04122024.txt", 'r')
#data_bestand = open("2024\\4 december\\Data\\Input_04122024_test.txt", 'r')
data = data_bestand.read().split()
#print(data)
#                NE     SE      SW        NW
directions = [[1, -1],[1, 1], [-1, 1], [-1, -1]]
nRows = len(data)
nColumns = len(data[0])
totalXmas = 0

"""def searchXmas(x, y, direction):
    dirX = direction[0]
    dirY = direction[1]
    if dirX == -1 and x < 3:
        return 0
    if dirX == 1 and x > nColumns - 4:
        return 0
    if dirY == -1 and y < 3:
        return 0
    if dirY == 1 and y > nRows - 4:
        return 0
    if not(data[y + dirY][x + dirX] == 'M'):
        return 0
    if not(data[y + (2 * dirY)][x + (2 * dirX)] == 'A'):
        return 0
    if not(data[y + (3 * dirY)][x + (3 * dirX)] == 'S'):
        return 0
    return 1
"""

def searchX_Mas(x, y):
    nMs = 0
    nSs = 0
    if x == 0 or x == nColumns - 1 or y == 0 or y == nRows - 1:
        return 0
    if data[y-1][x-1] == data[y+1][x+1]:
        return 0

    for direction in directions:
        if data[y + direction[1]][x + direction[0]] == 'M':
            nMs += 1
        if data[y + direction[1]][x + direction[0]] == 'S':
            nSs += 1

    if nMs == 2 and nSs == 2:
        return 1
    return 0 


for y in range(0,nRows):
    for x in range(0, nColumns):
        if data[y][x] == 'A':
#            print("A found a = " + str(x) + " y = " + str(y))
            totalXmas += searchX_Mas(x, y)

print(totalXmas)

    


