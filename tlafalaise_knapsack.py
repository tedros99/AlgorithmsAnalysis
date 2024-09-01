# Lafalaise, Tedros

# Get the maximum weight from the user
maxWeight = int(input("How much weight can the backpack hold? "))

# Init item list
itemList = [
    ('Banana', 1, 99),
    ('Chocolate Bar', 1, 13),
    ('Marble Vase', 15, 34),
    ('Old Painting', 7, 54),
    ('Stone Tablet', 55, 98),
    ('Gaming Laptop', 20, 56),
    ('Flat Screen TV', 35, 50)
]

# Print them out in a "pretty" manner
print("Here is the list of items that can be taken:")
for item in itemList:
    name, weight, value = item[0], item[1], item[2]
    print("Name:", name, "| Weight:", weight, "| Value:", value)
print()

# Get max length of a combination
maxLength = len(itemList)

# Init solutions and remaining combos arrays
solutions = []
remCombos = []

# Add single items as their own solution and combo
for item in itemList:
    solutions.append({item})
    remCombos.append({item})

# While we haven't gone through every single combo...
while len(remCombos) != 0:
    # Get the first combo in list
    currCombo = remCombos.pop(0)
    # For each possible additional item
    for item in itemList:
        # If we don't already have it in this combo
        if item not in currCombo:
            # Create new combo with current one and the new item
            newCombo = set()
            newCombo.update(currCombo)
            newCombo.add(item)
            # If this combo is not already a submitted solution
            if newCombo not in solutions:
                # Add it to the solutions list
                solutions.append(newCombo)
                # If this combo isn't the max length, add it to the remaining combos
                if len(newCombo) < maxLength:
                    remCombos.append(newCombo)

# Init the variables that will hold the best value and items
bestValue = 0
bestItems = []

# For each possible solution
for solution in solutions:
    currWeight = 0
    currValue = 0
    # Calculate its weight and value
    for item in solution:
        currWeight += item[1]
        currValue += item[2]
    # If its not too heavy and has better value than the previous solution
    if currWeight <= maxWeight and currValue > bestValue:
        # Set the variables accordingly
        bestValue = currValue
        bestItems = solution

# Print out the optimal solution
print("With the given weight capacity of", maxWeight, "...")
print("We were able to get the best possible value of", bestValue, "with the following items:")
for item in bestItems:
    name, weight, value = item[0], item[1], item[2]
    print("Name:", name, "| Weight:", weight, "| Value:", value)