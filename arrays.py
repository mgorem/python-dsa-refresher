monthly_expense = [2200, 2350, 2600, 2130, 2190]

# 1. In Feb, how many dollars you spent extra compare to January?
print("Extra money spent in February compared to January: ", monthly_expense[1]-monthly_expense[0])

# 2. Find out your total expense in first quarter (first three months) of the year.
print("Total Expense for the first quarter (First Three Months): ", monthly_expense[0]+monthly_expense[1]+monthly_expense[2])

# 3. Find out if you spent exactly 2000 dollars in any month
print("Did I spent 2000$ in any month? ", 2000 in monthly_expense)

# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
print("Adding July expense: ", monthly_expense.append(1980), monthly_expense)

# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this
monthly_expense[3] -= 200
print("Refund of item in April: ", monthly_expense[3])

