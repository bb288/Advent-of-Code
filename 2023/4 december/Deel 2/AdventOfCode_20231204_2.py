data_bestand = open("2023/4 december/Data/Input_20231204.txt")
data = data_bestand.read().split('\n') # Use split on \n instead of readlines(). This makes th \n dissapear 
#data = data[:4]
lengthData = len(data)

nCards = 0
# Make a dictonary with how many cards there are of each card
cards = {}
i=0
while i < lengthData:
    i+=1
    cards[i] = 1

# Remove the card + number
for card, line in enumerate(data):
    card += 1
#    print(card)
    nWinning = 0
    part = line.split(':')[1]
    winningNumbers = part.split('|')[0].split()
    myNumbers = part.split('|')[1].split()
    
    for number in myNumbers:
        if number in winningNumbers:
            nWinning += 1
#    print(nWinning)
    j = 0
    while j < nWinning:
        j += 1
        if card + j <= lengthData:
            cards[card + j] += cards[card]
        else:
            break
    nCards += cards[card]

#    print(cards)
print("Aantal kaarten: "+ str(nCards))
    