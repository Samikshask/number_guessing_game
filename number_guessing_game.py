import random

def number_guessing_game():
    print("🎰 Welcome to the Number Guessing Game!")
    print("Try to guess the secret number between 1 and 100.")
    
    total_score = 0  # Track total points
    max_rounds = 5   # Limit to 5 rounds
    
    for round_num in range(1, max_rounds + 1):
        print(f"\n🎯 Round {round_num} starts!")
        secret_number = random.randint(1, 100)  # Pick a random number
        attempts = 0  # Count user attempts
        round_score = 100  # Start each round with 100 points
        
        while True:
            try:
                guess = input("🔢 Enter your guess (1-100):").strip()
                
                # Check if input is a number
                if not guess.isdigit():
                    print("⚠️ Invalid input! Please enter a number.")
                    continue
                
                guess = int(guess)
                attempts += 1
                
                # Ensure the guess is within range
                if guess < 1 or guess > 100:
                    print("⚠️ Out of range! Please guess a number between 1 and 100.")
                    continue
                # Give feedback
                if guess < secret_number:
                    print("📉 Too low! Try again.")
                    round_score -= 10  # Deduct points
                elif guess > secret_number:
                    print("📈 Too high! Try again.")
                    round_score -= 10  # Deduct points
                else:
                    print(f"🎉 Correct! You guessed it in {attempts} attempts.")
                    print(f"🏆 You earned {round_score} points this round.")
                    total_score += max(round_score, 0)  # Ensure score doesn't go negative
                    break  # Exit the loop when guessed correctly
                
            except ValueError:
                print("⚠️ Invalid input! Please enter a valid number.")

        # Stop automatically after 5 rounds
        if round_num == max_rounds:
            break
        
        # Ask if player wants to continue
        play_again = input("\nDo you want to play another round? (yes/no): ").strip().lower()
        if play_again != "yes":
            break  # Exit if they don't want to continue

    # Display final results
    print("\n🎮 Game Over! Thanks for playing.")
    print(f"🏅 Your Total Score: {total_score}")

# Run the game
if __name__ == "__main__":
    number_guessing_game()
