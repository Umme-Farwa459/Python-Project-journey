import random

player1 = int(input("Enter 1 to take first turn, or 2 for computer to go first: "))

if player1 == 1:
    # Player sets the number, computer guesses
    player1Number = int(input("Set number of your choice (1000-9999): "))
    ComputerGuess = random.randint(1000, 9999)
    print(f"Computer guessed: {ComputerGuess}")

    if ComputerGuess == player1Number:
        print("Computer is a Mastermind!")
    else:
        print("You are the Mastermind!")

else:
    # Computer sets the number, player guesses
    ComputerPlayer = random.randint(1000, 9999)
    player1Guess = int(input("Guess the number (1000-9999): "))

    if player1Guess == ComputerPlayer:
        print("You are a Mastermind!")
    else:
        print("Computer is a Mastermind!")
