data_bestand = open("9 december/Data/Input_20231209.txt")
#data_bestand = open("9 december/Data/Input_test.txt")
data = data_bestand.read().split('\n') # Use split on \n instead of readlines(). This makes th \n dissapear 
#print(data) 

#data = data[0:2]

totalSum = 0
test = []

# funtion to check if every value is 0
def checkZeros(list):
    for k in list:
        if k == 0:
            continue
        else:
            return False
    return True

for line in data:
    line = line.split()
#    print(line)
    prev_track = []
    current_track = []
    first_points = []
    # Make a list of numbers
    for l, point in enumerate(line):
        l=l+1
        current_track.append(int(line[-l]))
#    print(current_track)
    while not checkZeros(current_track):
        prev_track = current_track
        current_track = []
        for j, point in enumerate(prev_track):
            if j == 0:
                prev_point = point
            elif j == len(prev_track) - 1:
                current_track.append(point - prev_point)
                first_points.append(point) 
                prev_point = point
            else:
                current_track.append(point - prev_point)
                prev_point = point
#        print(current_track)
#        print(first_points)

    # add all numbers in last_points to the total
    test.append(sum(first_points))
    totalSum += sum(first_points)
#    print(sum(last_points))

#print(test)
#print(len(test))
print(totalSum)        
        
        




