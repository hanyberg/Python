list = [1, 3, 5, 6, 4, 2, 7, 9, 8]
print(list)
x=int(input("What number do you want to know the position of in the list?"))

#print(list.index(x))

for number in range(len(list)):
    #print(number, list[number])
    if list[number]==x:
        print(number+1)
    #print (number + "is in position" + range + " on the list.")