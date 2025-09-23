import random
print("Hi! Welcome to the Number Guessing Game.\n You have 8 chances to guess the number . Let's start")

low=int(input("Enter the lower bound: "))
high=int(input("Enter the highest bound: "))

print(f"You have 8 chances to guess the random number between {low} and {high}. Let's start!")

num=random.randint(low,high)
ch=8              #Total allowed chances
gc=0              #Guess counter

while gc<ch:
    gc+=1
    guess=int(input("Enter your guess: "))

    if guess == num:
        print(f"Perfect! The number is {num}. You guessed it in {gc} attempts.")
        break

    elif gc >= ch and guess != num:
        print(f"Sorry! The number was {num}. Better luck next time.")

    elif(guess>num):
        print("High! Guess a lower number.")
    elif(guess<num):
        print("Low! Guess a higher number.")  

