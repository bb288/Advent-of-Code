# Data inlezen
data_bestand = open("2 december\Data\Input_02122023.txt", 'r')
data = data_bestand.read().splitlines()
#data = data[:3]

maxRed = 12
maxGreen = 13
maxBlue = 14
length = len(data)
i=0
sumGameId = 0

while i < length:
    gameId = i+1
    impossible = 0

    line = data[i].split(":")[1]
    draws = line.split(";")

    for draw in draws:
        red = draw.find("red")
        green = draw.find("green")
        blue = draw.find("blue")

        if red != -1:
            nRed = int(draw[red-3:red-1])
        else:
            nRed = 0
        
        if green != -1:
            nGreen = int(draw[green-3:green-1])
        else:
            nGreen = 0
        
        if blue != -1:
            nBlue = int(draw[blue-3:blue-1])
        else:
            nBlue = 0
        
        if (nRed > maxRed or nGreen > maxGreen or nBlue > maxBlue):
            impossible = 1
#            print(f"Game_id {gameId} is impossible")
            break
    

    
    if impossible == 0:
        sumGameId += gameId

    i += 1

print(sumGameId)
