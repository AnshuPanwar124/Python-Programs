import random
lst= ["s","w","g"]

chance = 10
no_of_chance=0
computer_point =0
human_point=0

print(" \t \t Snake,Water,Gun \n")
print("s for snake \nw for water \ng for gun")

while no_of_chance < chance:
    _input = input ("Snake, Water,Gun\n")
    _random = random.choice(lst)

    if _input == _random:
        print("Tie Both 0 point to each \n")

    elif _input == "s" and _random =="g":
        computer_point = computer_point +1
        print(f"your guess {_input} and computer guess {_random}\n")
        print("computer wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n")

    elif _input == "s" and _random =="w":
        human_point = human_point +1
        print(f"your guess {_input} and computer guess {_random}\n")
        print("Human wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n")

    elif _input == "w" and _random =="s":
        computer_point = computer_point +1
        print(f"your guess {_input} and computer guess {_random}\n")
        print("computer wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n")

    elif _input == "w" and _random =="g":
        human_point = human_point +1
        print(f"your guess {_input} and computer guess {_random}\n")
        print("Human wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n")

    elif _input == "g" and _random =="s":
        human_point = human_point +1
        print(f"your guess {_input} and computer guess {_random}\n")
        print("Human wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n")

    elif _input == "g" and _random =="w":
        computer_point = computer_point +1
        print(f"your guess {_input} and computer guess {_random}\n")
        print("computer wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n")

    else:
        print("you have input wrong \n")

    no_of_chance = no_of_chance+1
    print(f"{chance- no_of_chance} is left out of {chance}")

print("Game over")

if computer_point > human_point:
  print("Computer wins and you lost")

if computer_point < human_point:
   print("Human wins and computer lost")

if computer_point == human_point:
    print("match ties")

print(f"your point is {human_point} and computer point is {computer_point}")

 


    
