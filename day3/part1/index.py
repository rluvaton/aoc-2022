# List of rucksacks
with open("input.txt") as f:
  input_str = f.read()

# Split the string into a list of lines
lines = input_str.split("\n")

rucksacks = lines

# Compute the sum of the priorities of the items that appear in both compartments of each rucksack
sum = 0
for rucksack in rucksacks:
    # Compute the sets of items in the first and second compartments
    first_compartment = set(rucksack[:len(rucksack) // 2])
    second_compartment = set(rucksack[len(rucksack) // 2:])

    # Compute the intersection of the two sets
    common_items = first_compartment.intersection(second_compartment)

    # If there are no common items, we can skip this rucksack
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
