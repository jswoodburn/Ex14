import random
# get user input
def get_user_choice(question_string = "Enter your choice (r, p, or s): ", acceptable_answer = ['R','P','S']):
    while True:  # fails after 3 attempts?
        user_choice = input(question_string)
        if user_choice.upper() in acceptable_answer:
            return user_choice.upper()
        print(f"Your choice must be one of the letters: {acceptable_answer}.\n")

# convert user choice to word
def convert_user_choice(user_choice):
    full_words={'R':'rock',
                'P':'paper',
                'S':'scissors'
                }
    return full_words[user_choice]





# generate random number
def generate_comp_choice():
    comp_choice = random.randint(0,2)
# convert number to computer choice
    if comp_choice == 0:
        return 'rock'
    elif comp_choice == 1:
        return 'scissors'
    else:
        return 'paper'


# compare choices/decide winner


# print winner

