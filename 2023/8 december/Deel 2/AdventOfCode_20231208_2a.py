data_bestand = open("2023/8 december/Data/Input_20231208.txt")
#data_bestand = open("2023/8 december/Data/Input_test.txt")
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

def keyInDict(key, dict):
    if key in dict:
        return True
    return False

def findNextNode(node, step):
    newStep = step - 1
#    nextNodes = []
    while newStep >= len(path):
        newStep = newStep - len(path)
    if path[newStep] == "L":
        dir = 0
    else:
        dir = 1
#    for node in nodes:
    nextNode = map[node][dir]
    return nextNode, newStep # newStep is the location in the path. If newStep icw nextNode is already in ... we end the loop

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

# We find for each starting point how long a 'total' loop takes 
# (until it is the same as an earlier code + same step in line) and at what point there is 'Z' at the end. 
# With this we can calculate the minimum where each starting node has a 'Z' at the end

for node in startingNodes:
    nodeLoop = {}
    numberOfSteps = 0
    sContinue = 1
    currentNode = node
    while sContinue == 1:
        numberOfSteps += 1
#        print(currentNode, numberOfSteps)
        currentNode, currentStep = findNextNode(currentNode, numberOfSteps)
#        print(currentNode, currentStep)
        if keyInDict(currentNode + "_" + str(currentStep), nodeLoop):
            lastNode = currentNode + "_" + str(currentStep)
            sContinue = 0
        else:
            nodeLoop[currentNode + "_"+ str(currentStep)] = numberOfSteps
            sContinue = 1
#        elif currentNode.endswith('Z'):
#            nodeLoop[currentNode + "_" + str(currentStep)] = 1
#            sContinue = 1
#        else:
#            nodeLoop[currentNode + "_" + str(currentStep)] = 0
#            sContinue = 1
    lengthLoop = len(nodeLoop) - nodeLoop[lastNode] -1 #?
#    print(nodeLoop)
    print(nodeLoop.keys())
    print(len(nodeLoop))
    print(lastNode)
    print(nodeLoop[lastNode])
    print(lengthLoop)


'''
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

currentNode = startingNode
numberOfSteps = 0
while currentNode != 'ZZZ':
    numberOfSteps += 1
    currentNode = findNextNode(currentNode, numberOfSteps)
#    print(currentNode)

print(numberOfSteps)

'''