# create a function that takes in an integer number of days and returns the number of seconds in that timespan.

def timeconverter (days):
    return days * 86400

days=int(input("How many days?\n"))

seconds = timeconverter(days)

print("That is " + str(seconds) + " seconds.")