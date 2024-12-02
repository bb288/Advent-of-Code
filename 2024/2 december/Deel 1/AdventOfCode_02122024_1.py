# Data inlezen
data_bestand = open("2024\\2 december\Data\Input_02122024.txt", 'r')
#data_bestand = open("2024\\2 december\Data\Input_02122024_test.txt", 'r')
data_1 = data_bestand.read().split("\n")

data = []
for line in data_1:
    data.append(line.split())

def allIncreasing(report):
    nLevels = len(report)
    level = 0
    while level < nLevels - 1: #-1 last level doesn't have an next
        if not(int(report[level]) < int(report[level + 1])):
            return False
        level += 1
    return True

def allDecreasing(report):
    nLevels = len(report)
    level = 0
    while level < nLevels - 1: #-1 last level doesn't have an next
        if not(int(report[level]) > int(report[level + 1])):
            return False
        level += 1
    return True

def allInRange(report):
    nLevels = len(report)
    level = 0
    while level < nLevels - 1:
        if not(1 <= abs(int(report[level]) - int(report[level + 1])) <= 3):
            return False
        level += 1
    return True

totalCorrectReports = 0

for report in data:
    nLevels = len(report)
    if (allIncreasing(report) or allDecreasing(report)) and allInRange(report):
        totalCorrectReports += 1

print (totalCorrectReports)



