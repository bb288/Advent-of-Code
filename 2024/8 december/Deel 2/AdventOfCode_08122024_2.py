# Data inlezen
data_bestand = open("2024\\8 december\\Data\\Input_08122024.txt", 'r')
#data_bestand = open("2024\\8 december\\Data\\Input_08122024_test.txt", 'r')
data_1 = data_bestand.read().split()
data = []
for line in data_1:
    data.append(list(line))

frequencies = dict()
y = 0
while y < len(data):
#    print(data[y])
    x=0
    while x < len(data[y]):
        currentFrequency = data[y][x]
        if not(currentFrequency == '.'):
            if currentFrequency in frequencies.keys():
                frequencies[currentFrequency].append([x, y])
            else:
                frequencies[currentFrequency] = [[x, y]]
        x += 1
    y += 1

#print(frequencies)
antinodes = []
for key in frequencies.keys():
    i = 0
    for coor in frequencies[key]:
        x = coor[0]
        y = coor[1]
        for coor2 in frequencies[key][i+1:]:
#            print("Coor 1: " + str(coor))
#            print("Coor 2: " + str(coor2))
            x2 = coor2[0]
            y2 = coor2[1]
            j = 1
            k = 1
            if x > x2:
                while not(x2 + (j * (abs(x - x2))) >= len(data[0]) or y2 - (j * (abs(y - y2))) < 0):
                    antinodes.append([x2 + (j * (abs(x - x2))), y2 - (j * (abs(y - y2)))])
                    j += 1
                while not(x - (k * (abs(x - x2))) < 0 or y + (k * (abs(y - y2))) >= len(data)):
                    antinodes.append([x - (k * (abs(x - x2))), y + (k * (abs(y - y2)))])
                    k += 1
            else:   
                while not(x2 - (j * (abs(x - x2))) < 0 or y2 - (j * (abs(y - y2))) < 0):
                    antinodes.append([x2 - (j * (abs(x - x2))), y2 - (j * (abs(y - y2)))])
                    j += 1
                while not(x + (k * (abs(x - x2))) >= len(data[0]) or y + (k * (abs(y - y2))) >= len(data)):
                    antinodes.append([x + (k * (abs(x - x2))), y + (k * (abs(y - y2)))])
                    k += 1
        i += 1

seen = []
antinodesUniq = []
for coor in antinodes:
    if coor not in seen:
        seen.append(coor)
        antinodesUniq.append(coor)

#print(frequencies)
#print(antinodes)
#print(len(antinodes))
#print(antinodesUniq)
print(len(antinodesUniq))