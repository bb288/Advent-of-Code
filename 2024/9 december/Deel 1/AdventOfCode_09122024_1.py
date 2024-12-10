# Data inlezen
data_bestand = open("2024\\9 december\\Data\\Input_09122024.txt", 'r')
#data_bestand = open("2024\\9 december\\Data\\Input_09122024_test.txt", 'r')
data = data_bestand.read()

print(data)
print(len(data))

even = False
idNumber = 0
list = []

for char in data:
    if even:
        for j in range(0,int(char)):
            list.append('.')
        even = False
    else:
        for j in range(0,int(char)):
            list.append(idNumber)
        even = True
        idNumber += 1
        
def checkIfNumber(input):
    try:
        int(input)
        return True
    except:
        return False

def findLastNumber(list):
    j = len(list) - 1
    while j > 0:
        if list[j] == '.':
            list = list[:j]
        else:
            return list[:j], list[j]#, list[:j]
        j -= 1

totalSum = 0
idNumber = 0
while idNumber < len(list):
    if list[idNumber] == '.':
        list, list[idNumber] = findLastNumber(list)
        totalSum += idNumber * list[idNumber]
    else:
        totalSum += idNumber * list[idNumber]
    if idNumber % 1000 == 0:
        print(idNumber)
    idNumber += 1
print(totalSum)