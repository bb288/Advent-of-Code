data_bestand = open("2023/7 december/Data/Input_20231207.txt")
#data_bestand = open("2023/7 december/Data/Input_test.txt")
data = data_bestand.read().split('\n') # Use split on \n instead of readlines(). This makes th \n dissapear 

types_oms = ['fiveOfAKind', 'fourOfAKind', 'fullHouse', 'threeOfAKind', 'twoPair', 'onePair', 'highCard']
order = {'A': 'm', 'K': 'l', 'Q': 'k', 'T': 'j', '9': 'i', '8': 'h', '7': 'g', '6': 'f', '5': 'e', '4': 'd', '3': 'c', '2': 'b', 'J': 'a'}

types = {}

fiveOfAKind = []
fourOfAKind = []
fullHouse = []
threeOfAKind = []
twoPair = []
onePair = []
highCard = []

print(data)

def replaceHand(hand):
    for key in order.keys():
        hand = hand.replace(key, order[key])
    return hand

def keyInDict(key, dict):
    if key in dict:
        return True
    return False

def addHandToType(hand, bid):
    cards = {}
    if hand == 'JJJJJ':
        fiveOfAKind.append((replaceHand(hand), bid))
        return
    for card in hand:
        if card == 'J':
            continue
        elif hand.count(card) + hand.count('J') == 5:
            fiveOfAKind.append((replaceHand(hand), bid))
            return
        elif hand.count(card) + hand.count('J') == 4:
            fourOfAKind.append((replaceHand(hand), bid))
            return
        elif hand.count(card) == 3 and not keyInDict(card, cards):
            cards[card] = 3
        elif hand.count(card) == 2 and not keyInDict(card, cards):
            cards[card] = 2
    # If no Jokers do same as part one
    if hand.count('J') == 0:
        if len(cards) == 1 and max(cards.values()) == 2:
            onePair.append((replaceHand(hand), bid))
            return
        elif len(cards) == 1 and max(cards.values()) == 3:
            threeOfAKind.append((replaceHand(hand), bid))
            return
        elif len(cards) == 2 and max(cards.values()) == 2:
            twoPair.append((replaceHand(hand), bid))
            return
        elif len(cards) == 2 and max(cards.values()) == 3:
            fullHouse.append((replaceHand(hand), bid))
            return
        highCard.append((replaceHand(hand), bid))
    # If there are jokers in the hand
    if hand.count('J') > 0:
        cards['J'] = hand.count('J')
        if len(cards) == 1:
            if max(cards.values()) == 1:
                onePair.append((replaceHand(hand), bid))
                return
            elif max(cards.values()) == 2:
                threeOfAKind.append((replaceHand(hand), bid))
                return
        elif len(cards) == 2: # Here can only be three of a kinds. Because there is at least 1 J and 1 pair. Anything higher would be 4/5 of a Kind and is already handeld
            threeOfAKind.append((replaceHand(hand), bid))
            return
        elif len(cards) == 3: # Here can only be full house.
            fullHouse.append((replaceHand(hand), bid))
            return

for bet in data:
    hand, bid = bet.split()
    addHandToType(hand, bid)

def getFirstValue(bet):
    return bet[0]
# Sort everything from low to high:
highCard.sort(key=getFirstValue)
onePair.sort(key=getFirstValue)
twoPair.sort(key=getFirstValue)
threeOfAKind.sort(key=getFirstValue)
fullHouse.sort(key=getFirstValue)
fourOfAKind.sort(key=getFirstValue)
fiveOfAKind.sort(key=getFirstValue)

#print(highCard)
#print(onePair)
#print(twoPair)
#print(threeOfAKind)
#print(fullHouse)
#print(fourOfAKind)
#print(fiveOfAKind)

def getTotalWinnings(startNumber, type, totalWinnings):
    currentNumber = startNumber
    for i in range(len(type)):
        totalWinnings += currentNumber * int(type[i][1])
        currentNumber += 1
    return currentNumber, totalWinnings


totalWinnings = 0
currentNumber = 1
currentNumber, totalWinnings = getTotalWinnings(currentNumber, highCard, totalWinnings)
currentNumber, totalWinnings = getTotalWinnings(currentNumber, onePair, totalWinnings)
currentNumber, totalWinnings = getTotalWinnings(currentNumber, twoPair, totalWinnings)
currentNumber, totalWinnings = getTotalWinnings(currentNumber, threeOfAKind, totalWinnings)
currentNumber, totalWinnings = getTotalWinnings(currentNumber, fullHouse, totalWinnings)
currentNumber, totalWinnings = getTotalWinnings(currentNumber, fourOfAKind, totalWinnings)
currentNumber, totalWinnings = getTotalWinnings(currentNumber, fiveOfAKind, totalWinnings)
print(totalWinnings)
