prices = []

print("Enter prices of 6 items:")
for i in range(6):
    price = int(input(f"Item {i+1}: "))
    prices.append(price)

print()
budget = int(input("Enter total budget: "))
print()

current_total = 0
bought_items = []

for i in range(6):
    if current_total + prices[i] <= budget:
        current_total += prices[i]
        bought_items.append(prices[i])
        print(f"Item {i+1} = {prices[i]} -> buy")
        print(f"Current total = {current_total}")
    else:
        print(f"Item {i+1} = {prices[i]} -> cannot buy")
        print(f"Current total = {current_total}")
    print()

remaining_budget = budget - current_total

print(f"Bought items: {bought_items}")
print(f"Total spent: {current_total}")
print(f"Remaining budget: {remaining_budget}")