# Data inlezen
data_bestand = open("2 december\Data\Input_02122023.txt", 'r')
data = data_bestand.read().splitlines()
#data = data[:1]

length = len(data)
i=0
TotaleOutcome = 0

while i < length:
    highestRed = 0
    highestGreen = 0
    highestBlue = 0

    line = data[i].split(":")[1]
    draws = line.split(";")

    for draw in draws:
        red = draw.find("red")
        green = draw.find("green")
        blue = draw.find("blue")

        if red != -1:
            nRed = int(draw[red-3:red-1])
            if nRed > highestRed:
                highestRed = nRed
        
        if green != -1:
            nGreen = int(draw[green-3:green-1])
            if nGreen > highestGreen:
                highestGreen = nGreen
        
        if blue != -1:
            nBlue = int(draw[blue-3:blue-1])
            if nBlue > highestBlue:
                highestBlue = nBlue
            
    TotaleOutcome += (highestRed * highestGreen * highestBlue) 
    i += 1

print(TotaleOutcome)
