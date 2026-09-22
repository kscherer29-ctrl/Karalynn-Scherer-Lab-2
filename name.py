import random

game_number = random.randint(1,10)
#print(game_number)
attempts = 0

while(True):
    guess = int(input("Enter a number between 1 and 10: "))
    attempts += 1

    if guess > game_number:
        print("Too high")
    elif guess < game_number:
        print("Too low")
    else:
        print(f"You win! You guessed the correct number in {attempts} attempts.")
        break