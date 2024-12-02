import copy

# Data inlezen
data_bestand = open("2024\\2 december\\Data\\Input_02122024.txt", 'r')
#data_bestand = open("2024\\2 december\\Data\\Input_02122024_test.txt", 'r')
data_1 = data_bestand.read().split("\n")

#data_1 = data_1[:3]

maxLevels = 0
data = []
for line in data_1:
    data.append(line.split())
    if len(line.split()) > maxLevels:
        maxLevels = len(line.split())

def checkReport(report):
    nLevels = len(report)
    level = 0
    increasing = True
    decreasing = True
    noBigSteps = True
    while ((increasing or decreasing) and noBigSteps) and level < nLevels - 1:
        currentLevel = int(report[level])
        nextLevel = int(report[level + 1])
        if currentLevel >= nextLevel:
            increasing = False
        if currentLevel <= nextLevel:
            decreasing = False
        if not(1 <= abs(currentLevel - nextLevel) <= 3):
            noBigSteps = False
        level += 1
    if (increasing or decreasing) and noBigSteps:
        return True, 0
    else:
        return False, level - 1

totalCorrectReports = 0
badReports = []

for report in data:
    report_org = copy.deepcopy(report)
    reportCorrect, reportFault_org = checkReport(report)
    if reportCorrect:
        totalCorrectReports += 1
        continue

    report.pop(reportFault_org)
    reportCorrect, reportFault = checkReport(report)
    if reportCorrect:
        totalCorrectReports += 1
        continue
    report_org.pop(reportFault_org + 1)
    reportCorrect, reportFault = checkReport(report_org)
    if reportCorrect:
        totalCorrectReports += 1
        continue

print (totalCorrectReports)



