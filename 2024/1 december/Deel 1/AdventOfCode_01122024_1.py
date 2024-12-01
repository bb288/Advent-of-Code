# Data inlezen
data_bestand = open("2024\\1 december\Data\Input_01122024.txt", 'r')
data_1 = data_bestand.read().split()

leftList = True

firstList = []
secondList = []

for number in data_1:
    if leftList:
        firstList.append(int(number))
        leftList = False
    else:
        secondList.append(int(number))
        leftList = True

firstList.sort()
secondList.sort()

i = 0
totalDistance = 0

while i < len(firstList):
    totalDistance += abs(firstList[i] - secondList[i])
    i += 1

print(totalDistance)