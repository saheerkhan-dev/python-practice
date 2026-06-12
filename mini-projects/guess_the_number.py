secret = 7

guess = int(input("Guess the number (1 to 10): "))

if guess == secret:
    print("Correct! You guessed it.")
else:
    print("Wrong guess. The number was", secret)
