import random

min_random_number_limit = 5
max_random_number_limit = 19

def welcome_username_prompt(): 
    user_name = input("Bitte geben Sie Ihren Benutzernamen ein: ")
    print(f"Hallo {user_name}! Ich denke an eine Zahl zwischen {min_random_number_limit} und {max_random_number_limit}. Welche Zahl ist es?")

def try_input():
    while True:
        try: 
            guess = int(input(f"Bitte geben Sie eine Zahl zwischen {min_random_number_limit} und {max_random_number_limit} ein: "))
            if (min_random_number_limit > guess or guess > max_random_number_limit):
                raise ValueError
        except ValueError:
            print("Eingabe unzulaessig. ", end="")
            continue
        else:
            return guess

def guess_is_correct(random_number, guess, amount_of_tries):
    if guess > random_number:
        print("Dein Versuch ist zu hoch. Bitte versuche es nochmal: ", end="")

        return False
    
    if guess < random_number: 
        print("Dein Versuch ist zu niedrig. Bitte versuche es nochmal: ", end="")

        return False
    
    if guess == random_number:
        print(f"Wow. Punktlandung. :) Du hast {amount_of_tries} Versuche gebraucht.")

        return True
    
def main_game():
        welcome_username_prompt()
        random_number = random.randint(min_random_number_limit, max_random_number_limit)
        amount_of_tries = 1
        guess = try_input()
        while not guess_is_correct(random_number, guess, amount_of_tries):
            guess = try_input()
            amount_of_tries += 1

if __name__ == '__main__':
    main_game()
