import rps_functions

play_again = 'Y'
while play_again == 'Y': 
    user_choice = rps_functions.get_user_choice()
    user_choice_converted=rps_functions.convert_user_choice(user_choice)
    print(user_choice_converted)
    play_again = rps_functions.get_user_choice("Do you want to play again (Y/N): ", ['Y','N'])