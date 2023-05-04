"""
Text based game: Beagles
Gamer has 10 tries to guess a number.
Each guess will be accompanied by feedback based on user guess.
PIKO, FERMI, BAGLES
"""
from random import shuffle

#Define game constants
MAX_NUMBERS = 3

#Inform the user about the game
user_input = input(f'''
Hello gamer!
This is text based game: BAGLES
You have 10 tries to guess a number.
Number will consist of {MAX_NUMBERS} numbers. Example: 023 or 359
After each answer you'll recieve a podpowiedź. 
PIKO: One number is correct but in a wrong position.
FERMI: One number is correct but in a correct position.
BAGLES: None of numbers are correct.
Would you like to play? 
(yes / no): \n
''')


#Generate a random number for the game
def generate_number():
    number_chain = '0123456789'
    list_chain = list(number_chain)
    shuffle(list_chain)
    result = ''.join(list_chain)
    cut_result = result[0:MAX_NUMBERS]
    return cut_result

# Game setup
user_tries = 1
number_to_guess = generate_number()
print(number_to_guess)
prompt_failed = 'Niepoprawna odpowiedź. Spróbuj jeszcze raz.'
prompt_success = f'Poprawna odpowiedź! Gratuluję poprawna liczba to:' \
                 f' {number_to_guess}. Udało się po {user_tries} próbach.'
user_guess = ''

# Game Mechanics
while user_tries <= 10:
    user_guess = input(f'Zgadnij liczbę z zakresu 001 - 999\nPróba {user_tries}: ')
    user_tries += 1
    if user_guess != number_to_guess:
        print(prompt_failed)
    elif user_guess == number_to_guess:
        print(prompt_success)
        break

#TODO: User feedback based on input

