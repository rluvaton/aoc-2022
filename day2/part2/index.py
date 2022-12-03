# Open the input file and read its contents into a string
with open("input.txt") as f:
  input_str = f.read()

# Define a mapping from shapes to their corresponding scores
SHAPE_SCORES = {
    'A': 1,   # Rock
    'B': 2,   # Paper
    'C': 3    # Scissors
}

def calculate_score(opponent_shape, round_result):
    # Determine what shape we should play based on the round result
    if round_result == 'X':
        # We should lose the round, so choose the shape that would lose
        # against the opponent's shape
        if opponent_shape == 'A':
            our_shape = 'C'  # Rock loses to Scissors
        elif opponent_shape == 'B':
            our_shape = 'A'  # Paper loses to Rock
        else:
            our_shape = 'B'  # Scissors loses to Paper
    elif round_result == 'Y':
        # We should draw the round, so choose the same shape as the opponent
        our_shape = opponent_shape
    else:
        # We should win the round, so choose the shape that would win
        # against the opponent's shape
        if opponent_shape == 'A':
            our_shape = 'B'  # Rock wins against Paper
        elif opponent_shape == 'B':
            our_shape = 'C'  # Paper wins against Scissors
        else:
            our_shape = 'A'  # Scissors wins against Rock

    # Calculate the score for the round
    score = SHAPE_SCORES[our_shape]
    if round_result == 'X':
        score += 0  # We lost the round
    elif round_result == 'Y':
        score += 3  # The round was a draw
    else:
        score += 6  # We won the round

    return score

def calculate_total_score(strategy_guide):
    # Initialize the total score to 0
    total_score = 0

    # Split the strategy guide into individual lines
    lines = strategy_guide.strip().split('\n')

    # Loop over each line in the strategy guide
    for line in lines:
        # Split the line into the opponent's shape and the round result
        opponent_shape, round_result = line.split()

        # Calculate the score for the round and add it to the total
        total_score += calculate_score(opponent_shape, round_result)

    return total_score

# Define the strategy guide
strategy_guide = input_str

# Calculate the total score for the strategy guide
total_score = calculate_total_score(strategy_guide)

# Print the total score
print(total_score)
