# List of rucksacks
with open("input.txt") as f:
  input_str = f.read()

# Split the string into a list of lines
lines = input_str.split("\n")

# List of rucksacks
rucksacks = lines

# Compute the sum of the priorities of the items that appear in all three rucksacks in each group
sum = 0
for i in range(0, len(rucksacks), 3):
    # Compute the sets of items in each rucksack
    rucksack_1 = set(rucksacks[i])
    rucksack_2 = set(rucksacks[i + 1])
    rucksack_3 = set(rucksacks[i + 2])

    # Compute the intersection of the three sets
    common_items = rucksack_1.intersection(rucksack_2).intersection(rucksack_3)

    # If there are no common items, we can skip this group
    if len(common_items) == 0:
        continue

    # Compute the priority of the item with the highest priority
    highest_priority = 0
    for item in common_items:
        if item.islower():
            # Lowercase items have priorities 1 through 26
            priority = ord(item) - ord("a") + 1
        else:
            # Uppercase items have priorities 27 through 52
            priority = ord(item) - ord("A") + 27

        # Update the highest priority if necessary
        highest_priority = max(highest_priority, priority)

    # Add the highest priority to the sum
    sum += highest_priority

# Print the sum
print(sum)
