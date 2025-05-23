import random

computer_number = random.randint(1,100)
guessed_number = False
while guessed_number != True:
    player_number = int(input("Guess the number (1-100): "))
    if player_number == computer_number:
        guessed_number = True
        print("You win!")
        print(f"The number is {computer_number}")

    elif player_number > computer_number:
        print("Too High!")
    else:
        print("Too Low!")
