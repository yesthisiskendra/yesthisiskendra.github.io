stock = {"banana": 6, "apple": 0, "orange": 32, "pear": 15}
prices = {"banana": 4, "apple": 2, "orange": 1.5, "pear": 3}
stock["cherry"] = 19
prices["cherry"] = 3.5
for fruit in stock:
	print(fruit, stock[fruit])
groceries = ["apple", "banana", "pear"]
grocery_total = 0
for item in groceries:
	print(prices[item])
	grocery_total += prices[item]
print('grocery total:', grocery_total)
totals = []
for fruit in stock:
	print(prices[fruit] * stock[fruit])
	totals.append(prices[fruit] * stock[fruit])
print('total value in stock:', sum(totals))