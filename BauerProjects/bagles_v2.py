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
This is text based game: BEAGLES
You have 10 tries to guess a number.
Number will consist of {MAX_NUMBERS} numbers. Example: 023 or 359
After each answer you'll receive a response. 
\tPIKO: One number is correct but in a wrong position.
\tFERMI: One number is correct and in a correct position.
\tBEAGLES: None of numbers are correct nor in a correct position.
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
user_guess = ''

#User feedback based on input
def get_feedback(correct_number, guess_number):
    """Returns response in a form of a list based on user guess number
    :arg guess_number - user guess number
    :arg correct_number - correct number generated for the game
    """
    response = []
    i = 0
    for number in guess_number:
        pass_number = False
        if correct_number[i] == guess_number[i]:
            response.append('Fermi')
            pass_number = True
        elif number in correct_number[i:] and not pass_number:
            print(f"ucięta liczba: {correct_number[i:]}")
            print(f"sprawdzana liczba: {number}")
            response.append('Piko')
            #TODO: Piko bug to be fixed
        i += 1
    if not response:
        return 'Beagle'
    else:
        shuffle(response)
        return ' '.join(response)

# Game Mechanics
while user_tries <= 10:
    user_guess = input(f'Guess a number in a range of 001 - 999'
                       f'\nAnswer {user_tries}: ')
    feedback = get_feedback(correct_number=number_to_guess, guess_number=user_guess)
    if user_guess != number_to_guess:
        print(feedback)
    elif user_guess == number_to_guess:
        prompt_success = f'Correct Answer! Congratulations correct number is:' \
                         f' {number_to_guess}. You succeed after {user_tries} ' \
                         f'tries.'
        print(prompt_success)
        break
    user_tries += 1