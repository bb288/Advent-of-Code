# Data inlezen
data_bestand = open("2024\\3 december\\Data\\Input_03122024.txt", 'r')
#data_bestand = open("2024\\3 december\\Data\\Input_03122024_test.txt", 'r')
data_1 = data_bestand.read()
data = list(data_1)

#print(data)    

def checkIfNumber(string):
    try:
        int(string)
        return True
    except:
        return False

"""if checkIfNumber(','):
    print("Getal")
else:
    print("Geen getal")
"""
totalSum = 0
mulString = ""
doString =""
num1 = ""
num2 = ""
do = True
for char in data:
    if do:
        if char == 'm':
            mulString = "m"
        elif char == 'u' and mulString == "m":
            mulString = "mu"
        elif char == 'l' and mulString == "mu":
            mulString = "mul"
        elif char == '(' and mulString == "mul":
            mulString = "mul("
        elif checkIfNumber(char) and mulString == "mul(":
            num1 += char
            if len(num1) > 3:
                mulString = ""
                num1 = ""
        elif char == ',' and mulString == "mul(" and not(num1 == ""):
            mulString = "mul(,"
        elif checkIfNumber(char) and mulString == "mul(," and not(num1 == ""):
            num2 += char
            if len(num2) > 3:
                mulString = ""
                num1 = ""
                num2 = ""
        elif char == ')' and mulString == "mul(," and not(num1 == "") and not(num2 == ""):
            totalSum += int(num1) * int(num2)
            mulString = ""
            num1 = ""
            num2 = ""
        else:
            mulString = ""
            num1 = ""
            num2 = ""
        
        if char == 'd':
            doString = "d"
        elif char == 'o' and doString == "d":
            doString = "do"
        elif char == 'n' and doString == "do":
            doString = "don"
        elif char == "'" and doString == "don":
            doString = "don'"
        elif char == "t" and doString == "don'":
            doString = "don't"
        elif char == '(' and doString == "don't":
            doString = "don't("
        elif char == ')' and doString == "don't(":
            do = False
            doString = ""
        else:
            doString = ""

    else:
        if char == 'd':
            doString = "d"
        elif char == 'o' and doString == "d":
            doString = "do"
        elif char == '(' and doString == "do":
            doString = "do("
        elif char == ')' and doString == "do(":
            do = True
            doString = ""
        else:
            doString = ""


print(totalSum)