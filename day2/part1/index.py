# Define the shapes and their scores
SHAPES = {
    "A": (1, "Rock"),
    "B": (2, "Paper"),
    "C": (3, "Scissors"),
    "Z": (3, "Scissors"),
    "Y": (2, "Paper"),
    "X": (1, "Rock")
}


# Define the possible outcomes of a round and their scores
OUTCOMES = {
    "win": 6,
    "draw": 3,
    "lose": 0
}

# Read the strategy guide from the file
with open("input.txt", "r") as f:
    strategy_guide = f.read().splitlines()

# Initialize the total score
total_score = 0

# Simulate each round of the game using the strategy guide
for strategy in strategy_guide:
    # Split the strategy into opponent's shape and your response
    opponent_shape, your_response = strategy.split()

    # Get the scores for the shapes and the outcome of the round
    opponent_score, opponent_name = SHAPES[opponent_shape]
    your_score, your_name = SHAPES[your_response]
    outcome_score = 0
    if your_score == opponent_score:
        outcome = "draw"
    elif your_score == 1 and opponent_score == 3:
        outcome = "win"
    elif your_score == 2 and opponent_score == 1:
        outcome = "win"
    elif your_score == 3 and opponent_score == 2:
        outcome = "win"
    else:
        outcome = "lose"
    outcome_score = OUTCOMES[outcome]

    # Print the result of the round
    print("Opponent chose %s, you chose %s, %s" % (opponent_name, your_name, outcome))

    # Add the score for the round to the total score
    total_score += your_score + outcome_score

# Print the total score
print("Total score:", total_score)
