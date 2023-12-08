data_bestand = open("5 december/Data/Input_20231205.txt")
#data_bestand = open("5 december/Data/Input_test.txt")
data = data_bestand.read() # Use split on \n instead of readlines(). This makes th \n dissapear 

transformations_inp = ['seed-to-soil map:', 'soil-to-fertilizer map:', 'fertilizer-to-water map:', 'water-to-light map:', 'light-to-temperature map:', 'temperature-to-humidity map:', 'humidity-to-location map:']
transformations_var = ['seedToSoil', 'soilToFertilizer', 'ferilizerToWater', 'waterToLight', 'lightToTemperature', 'temperatureToHumidity', 'humidityToLocation']
lowestLocation = None

# Transform the input data to readable data
seeds = data[:data.find("seed-to-soil")].split()[1:]

transformations = {}

def splitValues(sList):
    returnList = []
    for i, value in enumerate(sList):
         returnList.append(list(map(int, value.split())))
    return returnList

for i, transformation in enumerate(transformations_inp):
    if i == len(transformations_inp)-1:
        transformations[transformations_var[i]] = splitValues(data[data.find(transformation):].split("\n")[1:])
    else:
        transformations[transformations_var[i]] = splitValues(data[data.find(transformation):data.find(transformations_inp[i+1])].split("\n")[1:-2])
#print(transformations)

def getNextTransformation(transformation, currentNumber):
    j = 0
#    print(" CurrentNumber = " + str(currentNumber))
    while j < (len(transformations[transformation])):
        #print("  Range = " + str(int(transformations[transformation][j][1])) + " - " + str(int(transformations[transformation][j][1]) + int(transformations[transformation][j][2]) - 1))
        if int(transformations[transformation][j][1]) <= currentNumber <= (int(transformations[transformation][j][1]) + int(transformations[transformation][j][2]) -1):
            return currentNumber + (int(transformations[transformation][j][0]) - int(transformations[transformation][j][1]))
        j+=1
    # If not in any range then return same number
    return currentNumber
        
def transform(Seed):
    newNumber = int(Seed)
    for transformation in transformations_var:
        newNumber = getNextTransformation(transformation, newNumber)
#        print(" After " + transformation + ": " + str(newNumber))
    return newNumber

for seed in seeds:
    location = transform(seed)
    if lowestLocation == None or lowestLocation > location:
        lowestLocation = location

print(lowestLocation)
