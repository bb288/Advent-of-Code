import math

data_bestand = open("6 december/Data/Input_20231206.txt")
#data_bestand = open("6 december/Data/Input_test.txt")
data = data_bestand.read().split('\n') # Use split on \n instead of readlines(). This makes th \n dissapear 

time_1 = data[0].split()[1:]
distance_1 = data[1].split()[1:]
time = ''
distance = ''

for i in range(len(time_1)):
    time += time_1[i]
    distance += distance_1[i]

time = int(time)
distance = int(distance)

totalOptions = 1

# Formula to to calculate distance (y), given max_time z and button press x: y = x(z-x)
# Solve the formula for x where y = the distance
# distance = pres * (max_time - pres) => -(pres)^2+(pres*max_time)-distance = 0 => pres^2 -(pres * max_time) - distance = 0
# This resolves in x(press) = (-max_time + Sqrt(max_time^2 + 4*distance)) / -2
# and              x(press) = ( max_time - Sqrt(max_time^2 - 4*distance)) / -2

def formula(max_time, dist):
    x1 = math.ceil((max_time - math.sqrt(max_time**2 - 4*dist)) / 2)
    x2 = math.floor((max_time + math.sqrt(max_time**2 - 4*dist)) / 2)
    return x1, x2

x1, x2 = formula(time, distance+0.0001)
print(x2-x1 + 1)

    



