n=18
number_of_guesses = 1

print("number of guesses is limited only to 9 times")
while(number_of_guesses<=9):
    guess_number = int(input("Guess the number : \n"))
    if guess_number<18:
        print("you entered less number Please input greater :\n")
    elif guess_number>18:
        print("you entered greater number Please input less :\n")
    else:
        print("you won \n")
        print(number_of_guesses,"number of guesse he took to finish")
        break
    print(9-number_of_guesses,"no. of gueeses left")
    number_of_guesses=number_of_guesses+1

if(number_of_guesses>9):
    print("Game over")

 