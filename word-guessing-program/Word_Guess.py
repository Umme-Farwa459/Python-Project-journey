import random
name=str(input("What is your name? "))
print("Good Luck!" ,name)

words=["rainbow","school","computer","programming","python","mathematics","condition","water","board"]

word=random.choice(words)

print("Guess the charachters: ")  
guesses=""
turns=12

while turns>0:
    failed=0

    for char in word:
        if char in guesses:
            print(char, end="")
        else:
            print("_")
            failed+=1

            if failed == 0:
                print("You win")
                print("The word is: ",word)
                break

            print()
            guess=input("Guess a charachter:")
            guesses+=guess

            if guess  not in word:

                turns-=1
                print("Wrong")
                print("You have ", +turns, "more guesses")

                if turns == 0:
                    print("You loose!")
                    print(word)


