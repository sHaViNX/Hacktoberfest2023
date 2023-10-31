# Item list with item names and their respective prices
item_prices = {
    "ceiling fan": 6200,
    "red soil": 12000,
    "metal": 20000,
    "brick": 38,
    "sea sand": 15200,
    "cement": 2320,
    "white cement": 9500,
    "red cement": 81000,
}

# Initialize variables to store the item names and total cost
item_names = []
total_cost = 0

# Read four item names as input
for _ in range(4):
    item_name = input()  # Input is case-sensitive
    item_names.append(item_name)
    item_name_lower = item_name.lower()
    if item_name_lower in item_prices:
        total_cost += item_prices[item_name_lower]

# Output the prices of selected items and the total cost
for item_name in item_names:
    item_name_lower = item_name.lower()
    if item_name_lower in item_prices:
        print(f"{item_prices[item_name_lower]}-->{item_name}")
    else:
        print(f"0-->{item_name}")

print(f"{total_cost}-->Total")
