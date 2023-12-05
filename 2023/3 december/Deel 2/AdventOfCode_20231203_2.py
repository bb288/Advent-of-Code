#'''import pandas as pd # Library to work with datasets

data_bestand = open("2023/3 december/Data/Input_20231203.txt")
data = data_bestand.read().split('\n') # Use split on \n instead of readlines(). This makes th \n dissapear 
#data = data[:3]
lengthDataset = len(data) # gebruik om niet buiten de boundries te gaan
widthLines = len(data[0])
#'''

# First find the '*' symbols for every * symbol we will search for the 
# numbers around if only two, multiply and at the '*'-symbol to the list

    

# This is a function that (if we find a number) will find the whole number and will give where it is placed 
def findNumber(sLineNumber, sPoint):
    sLine = data[sLineNumber-1]
    sContinue1 = 1
    sContinue2 = 1

    # Finding starting position number
    sStartPoint = sPoint
    while sContinue1 == 1:
        if sStartPoint-1 >= 0:
            if sLine[sStartPoint-1].isdigit():
                sStartPoint -= 1
                sContinue1 = 1
            else:
                sContinue1 = 0
        else:
            sContinue1 = 0

    sNumber = sLine[sStartPoint]
    # Finding whole number using new starting position number
    while sContinue2 == 1:
        if sStartPoint+1 < widthLines:
            if sLine[sStartPoint+1].isdigit():
                sStartPoint += 1
                sNumber += sLine[sStartPoint]
                sContinue2 = 1
            else:
                sEndNumberPos = sStartPoint
                sContinue2 = 0
        else:
            sEndNumberPos = sStartPoint
            sContinue2 = 0
    #print(sNumber)
    return int(sNumber), sStartPoint, sEndNumberPos

# In this function given the position of a number we will itterate all the neighbours
def findSymbol(sLineNumber, sStartNumberPos, sEndNumberPos):

    # Some alterations to the input data so secure it stays inside of the array
    if sStartNumberPos == 0:
        sStartNumberPos = 1

    if sEndNumberPos == widthLines-1:
        sEndNumberPos = widthLines-2

    # Look at the previous line
    if sLineNumber > 1:
        sLinePrevious = data[sLineNumber-2]
        
        for sPoint in sLinePrevious[sStartNumberPos-1:sEndNumberPos+2]: #sEndNumberPos + 1 doesnt include the last one here
            if sPoint != '.' and not sPoint.isdigit():
                return True                
    
    # Look in current line if there is a symbol
    sLine = data[sLineNumber-1]
       
    if sLine[sStartNumberPos-1] != '.' and not sLine[sStartNumberPos-1].isdigit():
        return True
    if sLine[sEndNumberPos+1] != '.' and not sLine[sEndNumberPos+1].isdigit():
        return True
    
    # Look in next line if there is a symbol
    if sLineNumber < lengthDataset:
        sLineNext = data[sLineNumber]
        
        for sPoint in sLineNext[sStartNumberPos-1:sEndNumberPos+2]: #sEndNumberPos + 1 doesnt include the last one here 
            if sPoint != '.' and not sPoint.isdigit():
                return True

    # if the function hasn't stopped yet, return false, then there is no symbol adjacent to the number    
    return False

# In this function we search for all the numbers around a star symbol
def findNumbersStar(sLineNumber, sStarPos):
    
    sNumbers = []

    # Some alterations to the input data so secure it stays inside of the array
    if sStarPos == 0:
        sStartStarPos = 1
        sEndStarPos = 0
    else:
        sStartStarPos = sStarPos
        sEndStarPos = sStarPos

    # Previous line:
    if sLineNumber > 1:
        sLinePrevious = data[sLineNumber-2]
        sStartNumPrev = None
                
        for i, sPoint in enumerate(sLinePrevious[sStartStarPos-1:sEndStarPos+2]): #sEndNumberPos + 1 doesnt include the last one here
            if sPoint.isdigit():
                sNum, sStartNum, sEndNum = findNumber(sLineNumber-1, sStartStarPos + i - 1)
                if sStartNum != sStartNumPrev:
                    sNumbers.insert(len(sNumbers), sNum)
                    sStartNumPrev = sStartNum
                    
    # Look in current line if there is a symbol
    sLine = data[sLineNumber-1]
       
    if sLine[sStartStarPos-1].isdigit():
        sNum, sStartNum, sEndNum = findNumber(sLineNumber, sStartStarPos-1)
        sNumbers.insert(len(sNumbers), sNum)
        sStartNumPrev = sStartNum

    if sLine[sEndStarPos+1].isdigit():
        sNum, sStartNum, sEndNum = findNumber(sLineNumber, sStartStarPos+1)
        sNumbers.insert(len(sNumbers), sNum)
        sStartNumPrev = sStartNum

    # Next line:
    if sLineNumber < lengthDataset:
        sLineNext = data[sLineNumber]
        sStartNumPrev = None

        for i, sPoint in enumerate(sLineNext[sStartStarPos-1:sEndStarPos+2]): #sEndNumberPos + 1 doesnt include the last one here
            if sPoint.isdigit():
                sNum, sStartNum, sEndNum = findNumber(sLineNumber+1, sStartStarPos + i - 1)
                if sStartNum != sStartNumPrev:
                    sNumbers.insert(len(sNumbers), sNum)
                    sStartNumPrev = sStartNum

    return sNumbers
    
# Loop over every token. Everytime we find a number we search how big it is and find the position. 
# After that we search for if in the positions around, there are other characters the numbers of .

lineNumber = 0
totalNumber = 0
for line in data:
    lineNumber += 1
#    print(lineNumber)
    i = 0
    lineLength = len(line)

#    print(line)
    while i < lineLength:
        point = line[i]
#        print(point)

        #if point.isdigit():
         #   startNumberPos = i
         #   # Find the whole number including the position
         #   number, startNumberPos, endNumberPos = findNumber(lineNumber, i) # functie nummer
         #   i = endNumberPos
         #   symbol = findSymbol(lineNumber, startNumberPos, endNumberPos)

         #   if symbol:
         #       totalNumber += number
        
        if point == '*':
            starPos = i
            numbers = []
            numbers = findNumbersStar(lineNumber, starPos)
            print(numbers)
            if len(numbers) == 2:
            #    totalNumber -= numbers[0]
            #    totalNumber -= numbers[1]
                totalNumber += numbers[0]*numbers[1]

        i += 1

print(totalNumber)
