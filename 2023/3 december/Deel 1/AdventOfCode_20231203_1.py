#'''import pandas as pd # Library to work with datasets

data_bestand = open("3 december/Data/Input_20231203.txt")
data = data_bestand.read().split('\n') # Use split on \n instead of readlines(). This makes th \n dissapear 
lengthDataset = len(data) # gebruik om niet buiten de boundries te gaan
widthLines = len(data[0])
#'''

# This is a function that (if we find a number) will find the whole number and will give where it is placed 
def findNumber(sLineNumber, sPoint):
    sLine = data[sLineNumber-1]
    sContinue = 1
    sNumber = sLine[sPoint]

    while sContinue == 1:
        if sPoint+1 < widthLines:
            if sLine[sPoint+1].isdigit():
                sPoint += 1
                sNumber += sLine[sPoint]
                sContinue = 1
            else:
                sEndNumberPos = sPoint
                sContinue = 0
        else:
            sEndNumberPos = sPoint
            sContinue = 0
    return int(sNumber), sEndNumberPos, sPoint

# In this function given the position of a number we will find if there is a symbol adjacent
def findSymbol(sLineNumber, sStartNumberPos, sEndNumberPos):
    
    # Some alterations to the input data so secure it stays inside of the array
    if sStartNumberPos == 0:
        sStartNumberPos = 1

    if sEndNumberPos == widthLines-1:
        sEndNumberPos = widthLines-2

    # Look at the previous line if there is a symbol
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


# Loop over every token. Everytime we find a number we search how big it is and find the position. 
# After that we search for if in the positions around, there are other characters the numbers of .

lineNumber = 0
totalNumber = 0
for line in data:
    lineNumber += 1
    print(lineNumber)
    i = 0
    lineLength = len(line)

#    print(line)
    while i < lineLength:
        point = line[i]

#        print(point)

        if point.isdigit():
            startNumberPos = i
            # Find the whol number including the position
            number, endNumberPos, i = findNumber(lineNumber, i) #str(point) #functie nummer
            symbol = findSymbol(lineNumber, startNumberPos, endNumberPos)

            if symbol:
                totalNumber += number

        i += 1

print(totalNumber)