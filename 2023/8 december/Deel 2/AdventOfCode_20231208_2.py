from math import lcm

#data = "test"
data = "real"
if data == "test":
    data_bestand = open("8 december/Data/Input_20231208.txt")
elif data == "real":
    data_bestand = open("8 december/Data/Input_20231208.txt")
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

# dictionarty for loops. In here we will add for each starting node all the nodes_currentstep which end on a 'Z' 
loopsZ = {}
loopsLength = {}
#startingNodes = startingNodes[0:2]

for node in startingNodes:
    numberOfSteps = 0
    nodeLoop = {}
    sContinue = 1
    loopsZ[node] = []
    currentNode = node
    currentStep = -1
    while sContinue == 1:
        numberOfSteps += 1
        prevNode = currentNode
        prevStep = currentStep
        currentNode, currentStep = findNextNode(currentNode, numberOfSteps)
        if keyInDict(currentNode + "_" + str(currentStep), nodeLoop):
            lastNode = currentNode + "_" + str(currentStep)
            sContinue = 0
        else:
            nodeLoop[currentNode + "_"+ str(currentStep)] = numberOfSteps
            sContinue = 1
        if currentNode.endswith('Z'):
            loopsZ[node] += (currentNode + "_" + str(currentStep), numberOfSteps)
            sContinue = 1

    lengthLoop = len(nodeLoop) - nodeLoop[lastNode] + 1
    loopsLength[node] = lengthLoop

# Find the number where every count is the same
# Use LCM to calculate
print(lcm(loopsZ['BBA'][1], loopsZ['BLA'][1], loopsZ['AAA'][1], loopsZ['NFA'][1], loopsZ['DRA'][1], loopsZ['PSA'][1]))
