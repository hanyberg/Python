import random
#number = random.randint(1,4)
#print(number)

#a="You will live long."
#b="You will find true love."
#c="Beware of false friends!"
#d="You should get a dog."

#print("This is your fortune:")

#if number ==1:
#    print(a)
#if number ==2:
#    print(b)
#if number ==3:
#    print(c)
#if number ==4:
#    print(d)



fortunes=["You'll live.", "You'll be rich.", "You'll have bad luck.", "You should quit your job."]
new_number = random.randint(0,3)
print("Your fortune is: "+ fortunes[new_number])