# Data inlezen
data_bestand = open("2024\\5 december\\Data\\Input_05122024.txt", 'r')
#data_bestand = open("2024\\5 december\\Data\\Input_05122024_test.txt", 'r')
data = data_bestand.read().split("\n")

orderings = []
updates = []
fillOrd = True

for line in data:
    if line == '':
        fillOrd = False
        continue
    if fillOrd:
        orderings.append([line.split('|')[0], line.split('|')[1]])
    else:
        updates.append(line.split(','))

def checkOrder(first, second):
    for order in orderings:
        if order[0] == first and order [1] == second:
            return True
    return False

def switchNumbers(array, place):
    oldFirst = array[place]
    oldSecond = array[place + 1]
    array[place] = oldSecond
    array[place + 1] = oldFirst
    return array

sumMiddleNumbers = 0

updatesWrong = []

for update in updates:
    nNumbers = len(update)
    i = 0
    while i < nNumbers - 1: # Last number doesn't need to be checked, nothing behind
        if not(checkOrder(update[i], update[i+1])):
            updatesWrong.append(update)
            break
        i += 1

for update in updatesWrong:
    nNumbers = len(update)
    correctUpdate = False
    update1= update
    while not(correctUpdate):
        i = 0
        while i < nNumbers - 1: # Last number doesn't need to be checked, nothing behind
            if not(checkOrder(update1[i], update1[i+1])):
                update1 = switchNumbers(update1, i)
                break
            i += 1
            if i == nNumbers - 1:
                correctUpdate = True
    sumMiddleNumbers += int(update[int((nNumbers - 1)/2)])

print(sumMiddleNumbers)

