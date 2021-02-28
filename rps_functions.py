# get user input
def get_user_choice(question_string = "Enter your choice (r, p, or s): ", acceptable_answer = ['R','P','S']):
    while True:  # fails after 3 attempts?
        user_choice = input(question_string)
        if user_choice.upper() in acceptable_answer:
            return user_choice.upper()
        print(f"Your choice must be one of the letters: {acceptable_answer}.\n")

# convert user choice to word


# generate random number


# convert number to computer choice


# compare choices/decide winner


# print winner

