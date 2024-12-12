# Data inlezen
data_bestand = open("2024\\9 december\\Data\\Input_09122024.txt", 'r')
#data_bestand = open("2024\\9 december\\Data\\Input_09122024_test.txt", 'r')
data = data_bestand.read()

even = False
idNumber = 0
list = []

for char in data:
    if even:
        pointArray = []
        for j in range(0,int(char)):
            pointArray.append('.')
        if len(pointArray) > 0:
            list.append(pointArray)
        even = False
    else:
        numberArray = []
        for j in range(0,int(char)):
            numberArray.append(idNumber)
        if len(numberArray) > 0:
            list.append(numberArray)
        even = True
        idNumber += 1

def replacePointsWithRange(list, finalList, counter):
    i = len(list) - 1
    lengthEmpty = len(list[counter])
    counterEmpty = 0
    while i > counter:
        if not((list[i][0] == '.' or list[i][0] == '*')) and len(list[i]) <= lengthEmpty:
            counterNumber = 0
            while counterNumber < len(list[i]):
                list[counter][counterEmpty] = '*'
                finalList.append(list[i][counterNumber])
                list[i][counterNumber] = '*'
                counterEmpty += 1
                counterNumber += 1
                lengthEmpty -= 1
        i -= 1
    if not(lengthEmpty == 0):
        i = 0
        while i < lengthEmpty:
            finalList.append('.')
            list[counter][counterEmpty] = '*'
            i += 1
    return list, finalList

counter = 0
finalList = []
while counter < len(list):
    if list[counter][0] == '.':
        list, finalList = replacePointsWithRange(list, finalList, counter)
    elif list[counter][0] == '*':
        i = 0
        while i < len(list[counter]):
            finalList.append('.')
            i += 1
    else:
        i = 0
        while i < len(list[counter]):
            finalList.append(list[counter][i])
            i += 1
    if counter % 100 == 0:
        print(counter)
    counter += 1

totalSum = 0
counter = 0
while counter < len(finalList):
    if not(finalList[counter] == '.'):
        totalSum += counter * finalList[counter]
    counter += 1

print(totalSum)