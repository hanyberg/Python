#Omvandla ord till Rövarspråk

ord=input("That word do you want to translate to Rövarspråk?\n")
lista1=[]

#print(list(ord))
delat_ord=list(ord)
#print(delat_ord)

vokal=["a", "e", "i", "o", "u", "y", "å", "ä", "ö"]

for i in delat_ord:
    if i not in vokal:
        lista1.append(i+"o"+i)
    else:
        lista1.append(i)

#print(lista1)

str1="".join(lista1) #sätter ihop strings i lista1 till en sammanhängande sträng dvs ett ord
print(str1)

