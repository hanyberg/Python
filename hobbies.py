hobbylista = []
hobby=input("What do you like to do?")
while hobby!="stop":
    hobbylista.append(hobby)
    hobby = input("What do you like to do?")
    print(hobbylista)
print("Your hobbies are: {}".format(hobbylista))

print("Your hobbies are " + ", ".join(hobbylista) + ".")

#rad 7 och 9 är två alternativa lösningar på problemet, där rad 9 är den snygga lösningen.