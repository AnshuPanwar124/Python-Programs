winning_number = 20

print("This is a number guessing game")
input_number = int(input("Guess your number between 1 to 100: "))

guess=1
game_over=False

while not game_over:
    if(winning_number==input_number):
        print(f"You win! and you guess the number in time", +guess)
        game_over=True

    else:
        if(winning_number>input_number):
            print("You guess two low!")
            guess +=1
            input_number=int(input("Guess again"))

        else:
            print("You Guess too high")
            guess +=1
            input_number=int(input("Guess again"))

