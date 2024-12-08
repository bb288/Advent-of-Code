# Data inlezen
data_bestand = open("2024\\7 december\\Data\\Input_07122024.txt", 'r')
#data_bestand = open("2024\\7 december\\Data\\Input_07122024_test.txt", 'r')
data = data_bestand.read().split("\n")

def makeMatrix(numberOfPlaces):
    matrix = []
    i = 0
    while i < numberOfplaces:
        if i == 0:
            matrix = ['*', '+', '|']
        else:
            j = 0
            for j in range(0, len(matrix)):
                oldValue = matrix[j]
                matrix[j] = oldValue + '*'
                matrix.append(oldValue + '+')
                matrix.append(oldValue + '|')
                j += 1
        i += 1
    return matrix


totalSumOfCorrectAnswers = 0
for line in data:
    print(line)
    lineData = line.split()
    neededAnswer = int(lineData[0][:len(lineData[0])-1])
    numberOfplaces = len(lineData) - 2
    matrix = makeMatrix(numberOfplaces)
    for option in matrix:
        answer = int(lineData[1])
        i = 2
        for char in option:
            if char == '*':
                answer = answer * int(lineData[i])
            elif char == '+':
                answer = answer + int(lineData[i])
            elif char == '|':
                answer = int(str(answer) + lineData[i])
            i += 1
        if answer == neededAnswer:
            totalSumOfCorrectAnswers += answer
            break

print(totalSumOfCorrectAnswers)

    