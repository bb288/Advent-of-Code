#data_bestand = open("2023/8 december/Data/Input_20231208.txt")
data_bestand = open("2023/8 december/Data/Input_test.txt")
data = data_bestand.read().split('\n') # Use split on \n instead of readlines(). This makes th \n dissapear 

path = data[0]

startingNodes = []
map = {}

for i in data[2:]:
    map[i[:3]] = (i[7:10], i[12:15])
    if i[:3].endswith('A'):
        startingNodes.append(i[:3])

#print(startingNodes)
#print(map)

def findNextNodes(nodes, step):
    newStep = step - 1
    nextNodes = []
    while newStep >= len(path):
        newStep = newStep - len(path)
    if path[newStep] == "L":
        dir = 0
    else:
        dir = 1
    for node in nodes:
        nextNodes.append(map[node][dir])
    return nextNodes

def allNodesEndsZ(nodes, num):
    for node in nodes:
        returnValue = False
        if node.endswith('Z'):
#            print(nodes)
 #           print(num)
            continue
        else:
            return False
    return True

currentNodes = startingNodes
numberOfSteps = 0
sContinue = 1
while sContinue == 1:
    numberOfSteps += 1
#    print(numberOfSteps)
    currentNodes = findNextNodes(currentNodes, numberOfSteps)
#    for i, node in enumerate(currentNodes):
#        currentNodes[i] = findNextNode(node, numberOfSteps)
#    print(currentNodes)
    if allNodesEndsZ(currentNodes, numberOfSteps):
        sContinue = 0
print(currentNodes)
print(numberOfSteps)

'''

        

currentNode = startingNode
numberOfSteps = 0
while currentNode != 'ZZZ':
    numberOfSteps += 1
    currentNode = findNextNode(currentNode, numberOfSteps)
#    print(currentNode)

print(numberOfSteps)

'''