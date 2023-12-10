data_bestand = open("2023/8 december/Data/Input_20231208.txt")
#data_bestand = open("2023/8 december/Data/Input_test.txt")
data = data_bestand.read().split('\n') # Use split on \n instead of readlines(). This makes th \n dissapear 

startingNode = 'AAA'
path = data[0]
map = {}

for i in data[2:]:
    map[i[:3]] = (i[7:10], i[12:15])

def findNextNode(node, step):
    newStep = step - 1
    while newStep >= len(path):
        newStep = newStep - len(path)
    
    if path[newStep] == "L":
        nextNode = map[node][0]
    elif path[newStep] == "R":
        nextNode = map[node][1]
    return nextNode

        

currentNode = startingNode
numberOfSteps = 0
while currentNode != 'ZZZ':
    numberOfSteps += 1
    currentNode = findNextNode(currentNode, numberOfSteps)
#    print(currentNode)

print(numberOfSteps)
