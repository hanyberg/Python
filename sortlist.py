osorterad_lista = [2, 6, 3, 0, 4, 13]
print("Osorterad lista: " + str(osorterad_lista))
minst = min(osorterad_lista)
print(minst)

lista2 = []
lista2.append(minst)
print("Sorterad lista: " + str(lista2))

len_original=len(osorterad_lista)

for number in range(len_original):
    print(number, osorterad_lista[number])
    if osorterad_lista[number] == 0:
        print(osorterad_lista[number])

osorterad_lista.remove(minst)







