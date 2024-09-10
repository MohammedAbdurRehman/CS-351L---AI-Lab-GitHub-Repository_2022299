def ai_number_guessing_game_dfs():
    # Player selects a number
    print("Think of a number between 1 and 100, and I (the AI) will try to guess it.")

    # Initial variables
    low = 1
    high = 100
    attempts = 0

    # Stack for DFS (initialize with the entire range)
    stack = list(range(low, high + 1))  # DFS will explore all numbers from low to high sequentially

    # Loop until the AI guesses the number correctly or the stack is empty
    while stack:
        # Pop the last number from the stack (deepest element first, simulating DFS)
        guess = stack.pop()
        attempts += 1

        print(f"AI's guess is: {guess}")
        feedback = input("Enter 'h' if too high, 'l' if too low, or 'c' if correct: ").lower()

        if feedback == 'c':
            print(f"I (AI) guessed the number in {attempts} attempts!")
            return
        elif feedback == 'h':
            # If too high, remove all higher numbers from the stack (skip exploration of higher numbers)
            stack = [x for x in stack if x < guess]
        elif feedback == 'l':
            # If too low, remove all lower numbers from the stack (skip exploration of lower numbers)
            stack = [x for x in stack if x > guess]

    print("Something went wrong!")

# Run the AI version with DFS behavior
ai_number_guessing_game_dfs()
