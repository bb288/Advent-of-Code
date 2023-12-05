data_bestand = open("2023/4 december/Data/Input_20231204.txt")
data = data_bestand.read().split('\n') # Use split on \n instead of readlines(). This makes th \n dissapear 
#data = data[:2]

totalWinnings = 0

# Remove the card + number
for line in data:
    nWinning = 0
    part = line.split(':')[1]
    winningNumbers = part.split('|')[0].split()
    myNumbers = part.split('|')[1].split()
    
    for number in myNumbers:
        if number in winningNumbers:
            if nWinning == 0:
                nWinning = 1
            else:
                nWinning *= 2
    
    totalWinnings += nWinning

print(totalWinnings)
#print(data)
