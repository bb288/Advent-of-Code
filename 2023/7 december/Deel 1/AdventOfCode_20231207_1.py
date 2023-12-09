data_bestand = open("2023/7 december/Data/Input_20231207.txt")
#data_bestand = open("2023/7 december/Data/Input_test.txt")
data = data_bestand.read().split('\n') # Use split on \n instead of readlines(). This makes th \n dissapear 

types_oms = ['fiveOfAKind', 'fourOfAKind', 'fullHouse', 'threeOfAKind', 'twoPair', 'onePair', 'highCard']
order = {'A': 'm', 'K': 'l', 'Q': 'k', 'J': 'j', 'T': 'i', '9': 'h', '8': 'g', '7': 'f', '6': 'e', '5': 'd', '4': 'c', '3': 'b', '2': 'a'}

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
    for card in hand:
        if hand.count(card) == 5:
            fiveOfAKind.append((hand, bid))
            return
        elif hand.count(card) == 4:
            fourOfAKind.append((hand, bid))
            return
        elif hand.count(card) == 3 and not keyInDict(card, cards):
            cards[card] = 3
        elif hand.count(card) == 2 and not keyInDict(card, cards):
            cards[card] = 2
    if len(cards) == 1 and max(cards.values()) == 2:
        onePair.append((hand, bid))
        return
    elif len(cards) == 1 and max(cards.values()) == 3:
        threeOfAKind.append((hand, bid))
        return
    elif len(cards) == 2 and max(cards.values()) == 2:
        twoPair.append((hand, bid))
        return
    elif len(cards) == 2 and max(cards.values()) == 3:
        fullHouse.append((hand, bid))
        return
    highCard.append((hand, bid))
    return

for bet in data:
    hand, bid = bet.split()
    hand = replaceHand(hand)
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
