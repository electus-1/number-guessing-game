from art import logo
from random import randint


def main():
    print(logo)
    print("Welcome to Guess The Number Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    print(f"Psst. The answer is {answer}.")
    difficulty = input('Choose a difficulty. Type "easy", "normal" or "hard": ')
    if difficulty == "easy":
        attempts = 10
    elif difficulty == "hard":
        attempts = 5
    else:
        attempts = 7
    print(f"You have {attempts} attempts in total.")
    while True:
        if attempts == 0:
            print("You've run out of guesses, you lose.")
            return False
        guess = int(input("Make a guess: "))

        if guess == answer:
            if answer == 42:
                print(
                    "Well done! The answer was the ultimate question of life, the universe, and everything."
                )
            else:
                print(f"Well done for beating the game! The answer was {answer}.")
            return True
        elif guess < answer:
            attempts -= 1
            print(
                f"Too low.\nGuess again.\nYou have {attempts} attempts remaining to guess the number."
            )
        elif guess > answer:
            attempts -= 1
            print(
                f"Too high.\nGuess again.\nYou have {attempts} attempts remaining to guess the number."
            )


while True:
    was_succesful = main()
    if was_succesful:
        wants_to_go_again = input('Do you want another challenge? Type "yes" or "no": ')
        if wants_to_go_again != "yes":
            break
    if not was_succesful:
        wants_to_go_again = input(
            'Do you want to give it another go? Type "yes" or "no": '
        )
        if wants_to_go_again != "yes":
            break
