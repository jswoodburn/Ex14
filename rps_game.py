import rps_functions
import time

games_played = 0
games_won = 0
while True:
    # get user input as a letter and convert to word
    user_choice = rps_functions.get_user_choice()
    user_choice_converted=rps_functions.convert_user_choice(user_choice)

    # generate comp choice
    comp_choice = rps_functions.generate_comp_choice()

    # choose winner
    print(f'You chose {user_choice_converted}...')

    print(f'The computer chooses...')
    time.sleep(2)
    print(f'{comp_choice.capitalize()}!\n')
    win_list = rps_functions.get_winner(user_choice_converted, comp_choice)
    print(win_list[1])

    # track how many games played
    games_won+=win_list[0]
    games_played+=1

    # does user want to play again?
    play_again = rps_functions.get_user_choice("Do you want to play again (Y/N): ", ['Y','N'])
    if play_again == 'N':
        break

print(f"\nYou won {games_won} out of {games_played} games that you played.")