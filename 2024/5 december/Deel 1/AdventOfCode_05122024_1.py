# Data inlezen
data_bestand = open("2024\\5 december\\Data\\Input_05122024.txt", 'r')
#data_bestand = open("2024\\5 december\\Data\\Input_05122024_test.txt", 'r')
data = data_bestand.read().split("\n")
#print(data)

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

#print("Helft van 3 = " + str((3+1)/2))
#print("Helft van 5 = " + str((5+1)/2))
#print("Helft van 7 = " + str((7+1)/2))
#print("Helft van 9 = " + str((9+1)/2))

sumMiddleNumbers = 0

for update in updates:
#    print(update)
    nNumbers = len(update)
    correctUpdate = True
    i = 0
    while i < nNumbers - 1: # Last number doesn't need to be checked, nothing behind
        if not(checkOrder(update[i], update[i+1])):
            correctUpdate = False
#            print("Incorrect")
            break
        i += 1
    if correctUpdate:
#        print(int(update[int((nNumbers - 1)/2)]))
        sumMiddleNumbers += int(update[int((nNumbers - 1)/2)])

print(sumMiddleNumbers)

