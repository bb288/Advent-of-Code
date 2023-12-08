# used the code of HexTree (https://gist.github.com/HexTree) code (https://gist.github.com/HexTree/d1a3a36cf794d5cee1d325a63ff26a98)

data_bestand = open("5 december/Data/Input_20231205.txt")
#data_bestand = open("5 december/Data/Input_test.txt")
data = data_bestand.read() # Use split on \n instead of readlines(). This makes th \n dissapear 

transformations_inp = ['seed-to-soil map:', 'soil-to-fertilizer map:', 'fertilizer-to-water map:', 'water-to-light map:', 'light-to-temperature map:', 'temperature-to-humidity map:', 'humidity-to-location map:']
transformations_var = ['seedToSoil', 'soilToFertilizer', 'ferilizerToWater', 'waterToLight', 'lightToTemperature', 'temperatureToHumidity', 'humidityToLocation']
lowestLocation = None

# Transform the input data to readable data
seeds_1 = data[:data.find("seed-to-soil")].split()[1:]

l = 0
seeds = []
while l < len(seeds_1):
    seeds.append([int(seeds_1[l]), int(seeds_1[l]) + int(seeds_1[l+1]) - 1])
    l += 2

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

def getNewRange(seeds, trans):
    newRange = []
    for rangeSeed in seeds:
        alteredRange = []
        startRangeSeed = rangeSeed[0]
        endRangeSeed = rangeSeed[1]
#        print(str(startRangeSeed) + ' + ' + str(endRangeSeed))
        for new, start, range in trans:
            startTrans = start
            endTrans = start + range - 1
#            print(str(startTrans) + ' + ' + str(endTrans))
#            print(new)
#            print(start)
#            print(range)
            if endRangeSeed < startTrans or endTrans < startRangeSeed:
                continue
            inRangeStart = max(startRangeSeed, startTrans)
            inRangeEnd = min(endRangeSeed, endTrans)
            alteredRange.append((inRangeStart, inRangeEnd))
            newRange.append((inRangeStart + new - start, inRangeEnd + new - start))
        # All the seeds we havent changed yet will have the same number
        # First check if there are any seeds altered
#        print(alteredRange)
        if alteredRange == []:
            newRange.append((startRangeSeed, endRangeSeed))
            continue
        alteredRange.sort()
        # First we check if there are any seeds left for the start of the changed range
        if startRangeSeed < alteredRange[0][0]:
            newRange.append((startRangeSeed, alteredRange[0][0]-1))
        # Then we check the same at the end
        if endRangeSeed > alteredRange[-1][1]:
            newRange.append((alteredRange[-1][1]+1, endRangeSeed))
        # There will be a lot of Er komen nu veel dubbele ranges in
#        print(newRange)
    return newRange

newSeeds = seeds
for trans in transformations.values():
    newSeeds = getNewRange(newSeeds, trans)
#    print(newSeeds)

print(min(newSeeds)[0])

