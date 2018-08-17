# create a password selector program that follows the flowcart in Exercises 3.2

#slumpa ett adjektiv ur en lista

#slumpa ett substantiv ur en lista

#slumpa ett tal mellan 0 och 100

#slumpa ett skiljetecken

#skapa ett säkert lösen

#visa detta lösen

#Fråga: Vill du ha ett nytt lösen? Y -> kör ovanstånde om igen. N -> slut.


def password (adjektiv, substantiv, tal, skiljetecken):
    return adjektiv+substantiv+str(tal)+skiljetecken

adjektiv_alt=["fin", "ful", "rolig", "tråkig", "snabb", "långsam", "trött", "pigg", "glad", "arg"]
substantiv_alt=["hatt", "stol", "katt", "hund", "soffa", "bil", "hus", "tak", "golv","vägg"]
skiljetecken_alt=[",", ".", ";", ":", "!", "?", "-", "_", "(", ")"]

ask=input("Do you want a secure password?\n")

# en loop som gör att yes gör så den kör om allt igen och allt annat avslutar
while ask == "yes":
    import random

    adjektiv_nr=random.randint(0,9)
    substantiv_nr=random.randint(0,9)
    skiljetecken_nr=random.randint(0,9)


    adjektiv=(adjektiv_alt[adjektiv_nr])
    substantiv=(substantiv_alt[substantiv_nr])
    tal=(random.randrange(100))
    skiljetecken=(skiljetecken_alt[skiljetecken_nr])

    #print(tal) #extra rad för att testa att randomisern funkar

    #print(adjektiv+substantiv+skiljetecken) #extra rad för att testa att randomisern funkar

    secure_password = password(adjektiv, substantiv, str(tal), skiljetecken)

    print("Förslag på nytt lösenord: " + secure_password)

    ask=input("Do you want a new password?\n")

