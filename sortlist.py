# UPPGIFT: Sortera en lista med siffror så de hamnar i stigande storleksordning


#osorterad_lista = [2, 6, 3, 0, 4, 13]
#print("Osorterad lista: " + str(osorterad_lista))
#minst = min(osorterad_lista)
#print(minst)

#lista2 = []
#lista2.append(minst)
#print("Sorterad lista: " + str(lista2))

#len_original=len(osorterad_lista)

#for number in range(len_original):
#   print(number, osorterad_lista[number])
#    if osorterad_lista[number] == 0:
#        print(osorterad_lista[number])

#osorterad_lista.remove(minst)


#ovan mina försäk. nedan en lösning från en stackowerflowtråd:

osorterad_lista = [2, 6, 3, 0, 4, 13]
print(osorterad_lista) #mitt tillägg för att se originallistan
sorterad_lista = []

#pga while-loop kommer den sluta loopa när listan är tom

while osorterad_lista:
    minimum = osorterad_lista[0]  # arbitrary number in list
    for x in osorterad_lista:
        if x < minimum:
            minimum = x
    sorterad_lista.append(minimum)
    osorterad_lista.remove(minimum)

print(sorterad_lista)






