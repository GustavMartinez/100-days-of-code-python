print("Welcome to the tip calculator!")

total_bill = float(input("What was the total bill? $\t"))
tip = int(input("How much tip would you like to give? 10%, 12%, or 15%?\t"))
num_person = int(input("How many people to split the bill?\t"))

tip_value = total_bill * (tip/100)
bill_and_tip = total_bill + tip_value
result = bill_and_tip/num_person

print("----------Calculation----------")
print(f"Total bill: ${total_bill}")
print(f"Tip value: ${tip_value}")
print(f"Each person should pay: ${result}")
