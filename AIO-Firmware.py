import random

# Function to start the number guessing game
def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100. Try to guess it!")
    
    # Random number generation
    number_to_guess = random.randint(1, 100)
    
    # Initialize attempt count
    attempts = 0
    
    while True:
        try:
            # User input for their guess
            user_guess = int(input("Enter your guess: "))
            attempts += 1
            
            # Check if guess is correct, too high, or too low
            if user_guess < number_to_guess:
                print("Too low! Try again.")
            elif user_guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid integer.")
            
# Run the game
number_guessing_game()
