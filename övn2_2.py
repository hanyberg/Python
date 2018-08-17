
def tipping (price):

    if int(price) > 100:
        #print("Hurrah")
       tip = int(price) * 1.05
    else:
        #print("Opps")
        tip = int(price) * 1.1
    return round(tip,1)


ask="y"
while ask!="no":
    price=input("How much does the meal cost?")
    tip_to_pay=tipping(price)
    print("For a meal that costs "+str(price)+" kr you should pay "+str(tip_to_pay) + " kr to include the appropriate amount of tip.")
    ask = input("Do you want help with tipping again?")
