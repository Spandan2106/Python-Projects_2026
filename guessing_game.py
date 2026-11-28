import random
def play_game():
  secret_number = random.randint(1, 50)
  attempts = 0
  max_attempts = 7
  print("Welcome to the Number Guessing Game!")
  print(f"Guess a number between 1 and 50. You have {max_attempts} attempts.")
  while attempts < max_attempts:
    try:
      guess = int(input("\nEnter your guess: "))
      attempts += 1

      if guess < secret_number:
        print("Too low! Try a higher number.")
      elif guess > secret_number:
        print("Too high! Try a lower number.")
      else:
        print(
            f"Correct! You guessed the number in {attempts} attempt(s)."
        )
        return
      remaining = max_attempts - attempts
      if remaining > 0:
        print(f"Attempts left: {remaining}")
    except ValueError:
      print("Please enter a valid whole number.")
  print(f"\nGame over! The secret number was {secret_number}.")
if __name__ == "__main__":
  play_game()
