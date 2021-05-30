#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python


print("Welcome to the tip calculator")

total = float(input("What was the total bill? $ "))
percent = int(input("What percentage of tip would you like to give? 10, 12, or 15? "))
people = int(input("How many guests are there to split the bill? "))
split = (total / people) * ((100 + percent) / 100)
# split = "{:.2f}".format(split)

print(f"Each person should pay ${'{:.2f}'.format(split)} ")