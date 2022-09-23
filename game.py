import random

computer_guessed_number = random.randint(1, 100)
continue_game = True
while(continue_game):
    user_guess = int(input("Uzmini skaitli starp 1 un 100:"))

    if user_guess == computer_guessed_number:
        print("Tu uzminēji!")
        continue_game = False
    elif user_guess < computer_guessed_number:
        print("Tu pa maz mini!")
    elif user_guess > computer_guessed_number:
        print("Tu pa daudz minēji! ")
    else:
        print("Kautkada kļūda ir!")
print("Game over!")
