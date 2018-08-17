# övn1_7. Simple Calculator, Create a simple calculator that can add, subtract, divide and multiply

# How it should work:
# ● Ask the user what type of calculation they want to perform
# ● Ask for the first number
# ● Ask for the second number
# ● Return the result to the user

def calculator(add, subtract, multiply, divide):
    if ask == "add":
        sum = ask2 + ask3
    if ask == "subtract":
        sum = ask2 - ask3
    if ask == "multiply":
        sum = ask2 * ask3
    if ask == "divide":
        sum = ask2 / ask3

    return round(sum,2)


ask=input("What type of calculation do you want to perform? Chose between add, subtract, multiply or divide?\n")

ask2=float(input("What is the first number?\n"))

ask3=float(input("What is the second number?\n"))


svar=calculator("add", "subtract", "multiply", "divide")

print("The answer is "+str(svar)+".")