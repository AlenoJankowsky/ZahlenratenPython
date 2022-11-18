import random

user_name = input("Bitte geben Sie Ihren Benutzernamen ein: ")
print(f"Hallo {user_name}! Ich denke an eine Zahl zwischen 1 und 20. Welche Zahl ist es?")

def main_game():
    random_number = random.randint(1, 20)
    guess_is_in_interval = guess > 0 and guess < 21

    while not guess_is_in_interval:
        guess = int(input("Bitte geben Sie eine Zahl zwischen 1 und 20 ein: "))
       
main_game()
