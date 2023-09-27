print("Behold: The Bill-Splitinator!")

bill = float(input("What was the total bill? \n$"))

percent = int(input("What percentage tip would you like to give?\n" ))

people = int(input("How many people are splitting the bill?\n"))

# GOOD!

percentDecimal = float(percent / 100)
# print(percentDecimal) GOOD!

percentBill = bill * percentDecimal

totalBill = bill + percentBill
# print(totalBill) GOOD!

split = totalBill / people
# print(split) GOOD!

splitDollar = round(split, 2)
# print(splitDollar) GOOD!

print(f"Each person should pay: ${splitDollar}")