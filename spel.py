score=0
print("Hello! Welcome to the Game of Locations!")
print("First question:")
answer=input("Where are you?")
if answer == "kivik" or answer == "Kivik":
    print("Good! You're right.")
    score=score+1
else:
    print("Sorry, you're wrong. Better luck next time.")
    score=score+0
print("Your current score is: " + str(score))
print("Second question:")
answer=input("What kind of fruit is grown here?")
if answer == "apple" or answer == "Apple" or answer == "apples" or answer == "Apples":
    print("Good! You're right.")
    score = score + 1
else:
    print("Sorry, you're wrong. Better luck next time.")
    score = score + 0
print("Your current score is: " + str(score))
answer=input("Do you wish to continue playing?")
if answer == "Yes" or answer == "yes" or answer == "Y" or answer == "y":
    print("Great! Let's see what you know about Malmö.")
    print("Third question:")
    answer = input("What kind of food is Malmö known for?")
    if answer == "Falafel" or answer == "falafel":
        print("Good! You're right.")
        score = score + 1
    else:
        print("Sorry, you're wrong. Better luck next time.")
        score = score + 0
    print("Your current score is: " + str(score))
elif answer == "No" or answer == "no" or answer == "N" or answer == "n":
    print("Sad to hear it. See you next time!")
else:
    print("Please answer with Yes or No")
    answer = input("Do you wish to continue playing?")
    if answer == "Yes" or answer == "yes" or answer == "Y" or answer == "y":
        print("Great! Let's see what you know about Malmö.")
    elif answer == "No" or answer == "no" or answer == "N" or answer == "n":
        print("Sad to hear it. See you next time!")