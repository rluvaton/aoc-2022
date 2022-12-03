# Open the input file and read its contents into a string
with open("input.txt") as f:
  input_str = f.read()

# Split the string into a list of lines
lines = input_str.split("\n")

# Read the input
calories = []
current_total = 0
max_total = 0
for line in lines:
  # If we encounter a blank line, we're done with this Elf's inventory
  if line.strip() == "":
    # Update the max total if necessary
    if current_total > max_total:
      max_total = current_total
    # Reset the current total for the next Elf
    current_total = 0
  else:
    # Parse the calorie count and add it to the current total
    current_total += int(line.strip())

# Print the maximum total
print(max_total)

