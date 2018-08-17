answer = input("Type in a number in deciliters:")

#cup_amount = float(answer)/2.37
#print(answer + " deciliters is equivalent to " + str(cup_amount) + " cups.")

#rad 3 och 4 är en enkel metod, nedan löses frågan med en funktion.

def cup_converter (dl_amount):
    return int(dl_amount) / 2.37

dl_amount = answer
cup_amount = cup_converter(dl_amount)
print(cup_amount)
print(answer + " dl is equal to " + str(cup_amount) + " cups.")
#print("That is equal to " + str(cup_amount) + " cups.")

#rad 14 och 15 är bara olika sätt att presentera samma lösning.


