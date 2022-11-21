import random

def welcome_username_prompt(): 
    user_name = input("Bitte geben Sie Ihren Benutzernamen ein: ")
    print(f"Hallo {user_name}! Ich denke an eine Zahl zwischen 1 und 20. Welche Zahl ist es?")

def try_input(amount_of_tries):
    while True:
            try: 
                if amount_of_tries == 1:
                    guess = int(input("Bitte geben Sie eine Zahl zwischen 1 und 20 ein: "))
                else: 
                    guess = int(input())

                if (guess < 1 or guess > 20):
                    raise ValueError
            except ValueError:
                if amount_of_tries == 1:
                    print("Eingabe unzulaessig.")
                else: 
                    print("Eingabe unzulaessig. Bitte geben Sie erneut eine Zahl zwischen 1 und 20 ein:  ", end="")
                continue
            else:
                return guess

def test_input(random_number, guess, amount_of_tries):
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
        random_number = random.randint(1, 20)
        amount_of_tries = 1
        guess = try_input(amount_of_tries)
        while not test_input(random_number, guess, amount_of_tries):
            guess = try_input(amount_of_tries)
            amount_of_tries += 1

main_game()
