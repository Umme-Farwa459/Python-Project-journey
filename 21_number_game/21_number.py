import random

numbers = list(range(1, 22))
print("Welcome to 21 Number game , You vs Computer")
user = input("Do you want to start the game (Yes/No): ")
choice = input("Enter 'F' to take the first chance and 'S' to take the second chance: ")
print(f"You took {choice} chance")

while True:
    # --- User turn ---
    user_input = input("Enter numbers of your choice (1-21, separated by commas): ")
    user_player = [int(num.strip()) for num in user_input.split(",")]

    if 21 in user_player:
        print("You lose! You entered 21")
        break

    # --- Computer turn ---
    computer_count = random.randint(1, 3)
    computer_player = random.sample(numbers, computer_count)

    if 21 in computer_player:
        print(f"Computer chose {computer_player}")
        print("Computer loses! It entered 21.")
        break

    # --- Show moves each round ---
    print(f"You chose {user_player}")
    print(f"Computer chose {computer_player}")
    print()
