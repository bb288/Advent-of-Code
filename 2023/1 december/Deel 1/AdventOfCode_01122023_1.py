# Data inlezen
data_bestand = open("Data\Input_01122023.txt", 'r')
data_1 = data_bestand.read().split()
data_1 = data_1[:2]
#print(data_1)

#print(type(data))
#print(type(data_1))
#print(data_1)

# functie om te checken of een letter een integer is
def is_integer(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return float(n).is_integer()

# loop over alle woorden en letters heen om te bepalen wat het eerste en laatste cijfer is
# Tel deze aan elkaar geplakt allemaal bij elkaar op om tot het totale aantal te komen 
totaal = 0
for word in data_1:
    eerste_cijfer = 0
    laatste_cijfer = 0
    cijfer = 0

    for letter in word:
        if is_integer(letter) and eerste_cijfer == 0:
            eerste_cijfer = int(letter)
            laatste_cijfer = int(letter)
        elif is_integer(letter):
            laatste_cijfer = int(letter)
    
    cijfer = int(str(eerste_cijfer) + str(laatste_cijfer))
    totaal += cijfer

# Het antwoord
print(totaal)


    

