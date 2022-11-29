#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator.")
bil = input("What was the total bill? $")
tip = input("What percentage tip would you like to give? 10, 12, or 15? ")
ppl = input("How many people to split the bill? ")

bil1 = float(bil)
tip1 = int(tip)
ppl1 = int(ppl)

bt = tip1 / 100
bilse = bil1 * bt
tbil = bil1 + bilse
splitb = tbil / ppl1
total = round(splitb,2)
total = "{:.2f}".format(splitb)

print(f"Each person should pay: ${total}")
