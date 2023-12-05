# Data inlezen
data_bestand = open("Data\Input.txt", 'r')
data_1 = data_bestand.read().split()
#data_1 = data_1[:2]



cijfers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
cijfers_3 = ['one', 'two', 'six']
cijfers_4 = ['four', 'five', 'nine']
cijfers_5 = ['three', 'seven', 'eight']


# functie om te checken of een letter een integer is
def is_integer(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return float(n).is_integer()

# om te checken of string een nummer is
def is_number(s):
    if s[len(s) - 3:] in cijfers_3:
        return translate_number(s[len(s) - 3:])
    elif s[len(s) - 4:] in cijfers_4:
        return translate_number(s[len(s) - 4:])
    elif s[len(s) - 5:] in cijfers_5:
        return translate_number(s[len(s) - 5:])
    else:
        return "No number"

# functie om geschreven nummers om te zetten naar integers
def translate_number(s):
    match s:
        case "one":
            return 1
        case "two":
            return 2
        case "three":
            return 3
        case "four":
            return 4
        case "five":
            return 5
        case "six":
            return 6 
        case "seven":
            return 7
        case "eight":
            return 8
        case "nine":
            return 9

# loop over alle woorden en letters heen om te bepalen wat het eerste en laatste cijfer is
# Tel deze aan elkaar geplakt allemaal bij elkaar op om tot het totale aantal te komen 
totaal = 0
for word in data_1:
    eerste_cijfer = 0
    laatste_cijfer = 0
    cijfer = 0

    deel_woord = ''

    for letter in word:
        deel_woord += letter
#        print(deel_woord)
#        print(is_number(deel_woord))



#        if deel_woord[laatste_3] in cijfers_3:
#            cijfer = cijfer_int


#        check of laatste 3, 4, 5 geschreven nummer


        if is_integer(letter) and eerste_cijfer == 0:
            eerste_cijfer = int(letter)
            laatste_cijfer = int(letter)
        elif is_integer(is_number(deel_woord)) and eerste_cijfer == 0:
            eerste_cijfer = is_number(deel_woord)
            laatste_cijfer = is_number(deel_woord)
        elif is_integer(letter):
            laatste_cijfer = int(letter)
        elif is_integer(is_number(deel_woord)):
            laatste_cijfer = is_number(deel_woord)
#        print(eerste_cijfer)
#        print(laatste_cijfer)
    
    cijfer = int(str(eerste_cijfer) + str(laatste_cijfer))
    totaal += cijfer

# Het antwoord
print(totaal)


    

