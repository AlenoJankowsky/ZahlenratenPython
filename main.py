import random

# user_name = input("Bitte geben Sie Ihren Benutzernamen ein: ")
# print(f"Hallo {user_name}! Ich denke an eine Zahl zwischen 1 und 20. Welche Zahl ist es?")

def main_game():
    random_number = random.randint(1, 20)
    while True:
        try: 
            guess = int(input("Bitte geben Sie eine Zahl zwischen 1 und 20 ein: "))
            if guess < 1 or guess > 20:
                raise ValueError
        except ValueError:
            print("Eingabe unzulaessig. ")
            continue
        else:
            break
    
    

main_game()
