secret = 7

while True:
    guess = int(input("Guess the number (1 to 10): "))

    if guess == secret:
        print("Correct! You guessed it.")
        break
    else:
        print("Wrong guess, try again.")
