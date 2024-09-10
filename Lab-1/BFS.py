from collections import deque
import random

def ai_number_guessing_game_bfs():
    # Player selects a number
    print("Think of a number between 1 and 100, and I (the AI) will try to guess it.")
    low = 1
    high = 100
    attempts = 0

    # Queue for BFS
    queue = deque([(low, high)])

    while queue:
        low, high = queue.popleft()
        if low > high:
            continue

        guess = (low + high) // 2  # AI makes a guess in the middle of the range
        attempts += 1

        print(f"AI's guess is: {guess}")
        feedback = input("Enter 'h' if too high, 'l' if too low, or 'c' if correct: ").lower()

        if feedback == 'c':
            print(f"I (AI) guessed the number in {attempts} attempts!")
            return
        elif feedback == 'h':
            queue.append((low, guess - 1))  # If too high, add the lower range to the queue
        elif feedback == 'l':
            queue.append((guess + 1, high))  # If too low, add the upper range to the queue

    print("Something went wrong!")

# Run the AI version with BFS
ai_number_guessing_game_bfs()
