import random

MIN_NUM = 1
MAX_NUM = 100
BOUNDARY_VALUE = 10


def welcome_username_prompt():
    user_name = input("Bitte geben Sie Ihren Benutzernamen ein: ")
    print(
        f"Hallo {user_name}! Ich denke an eine Zahl zwischen {MIN_NUM} und {MAX_NUM}. Welche Zahl ist es?"
    )


def prompt_input():
    while True:
        try:
            guess = int(
                input(
                    f"Bitte geben Sie eine Zahl zwischen {MIN_NUM} und {MAX_NUM} ein: "
                )
            )
            if MIN_NUM > guess or guess > MAX_NUM:
                raise ValueError
            return guess
        except ValueError:
            print("Eingabe unzulaessig. ", end="")
            continue


def guess_is_correct(random_number, guess, amount_of_tries):
    guess_is_out_of_bound = (
        guess > random_number + BOUNDARY_VALUE or guess < random_number - BOUNDARY_VALUE
    )
    first_guess_is_in_lower_bound = (
        guess > random_number - BOUNDARY_VALUE and guess < random_number
    )
    first_guess_is_in_upper_bound = (
        guess < random_number + BOUNDARY_VALUE and guess > random_number
    )
    first_guess_is_in_bound = (
        first_guess_is_in_lower_bound or first_guess_is_in_upper_bound
    )
    is_first_check = True

    if guess_is_out_of_bound and is_first_check:
        print("Kalt. ", end="")
        is_first_check = False

        return False

    if first_guess_is_in_bound and is_first_check:
        print("Warm. ", end="")
        is_first_check = False

        return False

    if guess == random_number:
        print(f"Wow. Punktlandung. :) Du hast {amount_of_tries} Versuche gebraucht.")

        return True


def main_game():
    welcome_username_prompt()
    random_number = random.randint(MIN_NUM, MAX_NUM)
    amount_of_tries = 1
    guess = prompt_input()
    while not guess_is_correct(random_number, guess, amount_of_tries):
        guess = prompt_input()
        amount_of_tries += 1


if __name__ == "__main__":
    main_game()
