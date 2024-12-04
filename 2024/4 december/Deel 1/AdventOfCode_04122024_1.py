# Data inlezen
data_bestand = open("2024\\4 december\\Data\\Input_04122024.txt", 'r')
#data_bestand = open("2024\\4 december\\Data\\Input_04122024_test.txt", 'r')
data = data_bestand.read().split()
print(data)
#                N        NE       E      SE      S       SW        W        NW
directions = [[0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1]]
nRows = len(data)
nColumns = len(data[0])
totalXmas = 0

def searchXmas(x, y, direction):
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

for y in range(0,nRows):
    for x in range(0, nColumns):
        if data[y][x] == 'X':
            print("X found x = " + str(x) + " y = " + str(y))
            for direction in directions:
                totalXmas += searchXmas(x, y, direction)

print(totalXmas)

    


