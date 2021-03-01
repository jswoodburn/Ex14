import rps_functions
import time

games_played = 0
games_won = 0
comp_wins = 0

while True:
    # get user input as a letter and convert to word
    user_choice = rps_functions.get_user_choice()
    user_choice_converted = rps_functions.convert_user_choice(user_choice)

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
    games_played += 1
    if win_list[0] > 0:  # if the player has won
        games_won += 1
    if win_list[0] < 0:  # if the computer has won
        comp_wins += 1

    # scorekeeping
    compare_scores = games_won - comp_wins
    add_on = ['.', ' to you.', ' to the computer.']
    # add_on = lambda compare_scores: ' to you.' if compare_scores > 0 else (' to the computer.' if compare_scores < 0 else '.')
    if compare_scores > 0:
        print(f"So far the score is {games_won}:{comp_wins}{add_on[1]}")
    elif compare_scores < 0:
        print(f"So far the score is {comp_wins}:{games_won}{add_on[2]}")
    else:
        print(f"The score is a draw - it's {comp_wins} all.")

    # does the user want to play again
    play_again = rps_functions.get_user_choice("Do you want to play again (Y/N): ", ['Y', 'N'])
    if play_again == 'N':
        break

print(f"\nYou won {games_won} out of {games_played} games that you played.")
