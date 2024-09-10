import random

def ai_number_guessing_game_golden_ratio():
    # Player selects a number
    print("Think of a number between 1 and 100, and I (the AI) will try to guess it.")
    low = 1
    high = 100
    attempts = 0

    # Golden ratio
    phi = (1 + 5 ** 0.5) / 2

    while low <= high:
        # Calculate the golden ratio point
        guess = int(high - (high - low) / phi)
        attempts += 1

        print(f"AI's guess is: {guess}")
        feedback = input("Enter 'h' if too high, 'l' if too low, or 'c' if correct: ").lower()

        if feedback == 'c':
            print(f"I (AI) guessed the number in {attempts} attempts!")
            return
        elif feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print("Something went wrong!")

# Run the AI version with Golden Ratio
ai_number_guessing_game_golden_ratio()
