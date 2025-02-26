#TIP CALCULATOR
print("Welcome to the tip calculator!")
total_bill = float(input("what was the total bill? $"))
tip = int(input("how much tip would you like to give? 10,12 or 15? "))
split_bill = int(input("how many people to split the bill? "))
tip_cal = tip/100 * total_bill + total_bill
cal = (tip_cal/split_bill)
print(f"Each person should pay ${round(cal, 2)}")