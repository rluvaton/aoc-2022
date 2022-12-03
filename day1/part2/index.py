# Open the input file and read its contents into a string
with open("input.txt") as f:
  input_str = f.read()

# split the list of food items into groups, one group for each Elf
groups = input_str.split("\n\n")

# calculate the total number of Calories carried by each Elf
elf_calories = []
for group in groups:
  # split the group of food items into a list of individual items
  items = group.split("\n")

  # calculate the total number of Calories carried by this Elf
  total_calories = 0
  for item in items:
    total_calories += int(item)

  # add the total number of Calories carried by this Elf to the list
  elf_calories.append(total_calories)

# sort the Elves by the number of Calories they are carrying in descending order
elf_calories.sort(reverse=True)

# take the top three Elves and sum their Calories to find the answer to the problem
answer = elf_calories[0] + elf_calories[1] + elf_calories[2]

print(answer)