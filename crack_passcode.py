import itertools

# variable to keep track of number of guesses 
num_guesses = 0

# Function to check if the combination matches the target combination
def check_combination(test_combo, target_combo):
    global num_guesses
    # increment the number of guesses with each failed attempt
    num_guesses += 1
    # check if the current combination matches the target combination
    if test_combo == target_combo:
        return True
    else:
        return False

# Function to crack the padlock passcode
def crack_padlock(passcode):
    # Create a list of all possible combinations using the digits 1-9
    all_combinations = [''.join(combo) for combo in itertools.product('123456789', repeat=3)]
    # Iterate through all possible combinations
    for combo in all_combinations:
        # check if current combination matches the target combination
        if check_combination(combo, passcode):
            return True
    return False

if __name__ == "__main__":
    # Example target passcode
    passcode = "234"
    if crack_padlock(passcode):
        print("Padlock passcode cracked.")
        print(f"Number of guesses before success: {num_guesses}")
    else:
        print("Failed to crack padlock passcode.")
