# Data inlezen
#data_bestand = open("2023\\13 december\\Data\\Input_13122023_test.txt", 'r')
data_bestand = open("2023\\13 december\\Data\\Input_13122023.txt", 'r')
data = data_bestand.read().split("\n")

patterns = {}
patternNumber = 1
patterns[patternNumber] = []

# Split data in different patterns
for line in data:
    if line == "":
        patternNumber += 1
        patterns[patternNumber] = []
    else:
        patterns[patternNumber].append(line)

def sameArrays(array1, array2):
    i = 0
    while i < len(array1):
        if array1[i] != array2[i]:
            return False
        i += 1
    return True

def findReflectionsRows(pattern):
    reflections = []
    i = 1 # start at the second and check if they are simmilar with i-1
    while i < len(pattern):
        if sameArrays(pattern[i], pattern[i-1]):
            reflections.append(i)
        i += 1
    return reflections

def makeColumn(pattern, columnIndex):
    column = ""
    for line in pattern:
        column += line[columnIndex]
    return column

def findReflectionsColumns(pattern):
    reflections = []
    columnIndex = 1 # start at the second column and check if they are similar with the one before
    while columnIndex < len(pattern[0]):
        if sameArrays(makeColumn(pattern, columnIndex - 1), makeColumn(pattern, columnIndex)):
            reflections.append(columnIndex)
        columnIndex += 1
    return reflections

def mirrorArray(array):
    i = len(array) - 1
    mirroredArray = []
    while i >= 0:
        mirroredArray.append(array[i])
        i -= 1
    return mirroredArray

def checkReflectionRow(pattern, reflectionRow):
    leftPattern = pattern[:reflectionRow]
    leftPattern = mirrorArray(leftPattern)
    rightPattern = pattern[reflectionRow:]

    shortestPattern = min(len(leftPattern), len(rightPattern))

    i = 0
    while i < shortestPattern:
        if not(sameArrays(leftPattern[i], rightPattern[i])):
            return False, 0
        i += 1
    return True, len(leftPattern)

def checkReflectionColumn(pattern, reflectionColumn):
    leftNumbers = range(0, reflectionColumn)
    leftNumbers = mirrorArray(leftNumbers)
    rightNumbers = range(reflectionColumn, len(pattern[0]))

    shortestPattern = min(len(leftNumbers), len(rightNumbers))

    i = 0
    while i < shortestPattern:
        if not(sameArrays(makeColumn(pattern, leftNumbers[i]), makeColumn(pattern, rightNumbers[i]))):
            return False, 0
        i += 1
    return True, len(leftNumbers)

totalSum = 0

for patternIndex in patterns:
    pattern = patterns[patternIndex]
    reflectionsRows = findReflectionsRows(pattern)
    for reflectionRow in reflectionsRows:
        reflectionCorrect, reflectionLength = checkReflectionRow(pattern, reflectionRow)
        if reflectionCorrect:
            totalSum += reflectionLength * 100
    
    reflectionsColumns = findReflectionsColumns(pattern)    
    for reflectionColumn in reflectionsColumns:
        reflectionCorrect, reflectionLength = checkReflectionColumn(pattern, reflectionColumn)
        if reflectionCorrect:
            totalSum += reflectionLength

print(totalSum)
