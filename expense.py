n = int(input("Enter no of peoples :"))
expense = {}
for i in range(n):
    a = input("Enter the name :")
    b = int(input("Enter the amount :"))
    expense[a] = b

list2 = list(expense.values())

avg = (float(sum(list2)/float(n)))
list3 = list(expense.keys())
expense_diff = {}
for i in range(n):
    x = avg-list2[i]
    expense_diff[list3[i]] = x
print(expense_diff)