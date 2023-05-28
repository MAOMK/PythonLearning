# Rock vs Paper vs Scissors
import ui as ui
import game_logic as game



def play_game():
    user_score = 0
    pc_score = 0
    round_number = 0
    # Define rounds -> Global Scope
    max_rounds = 5
    # Define score to win
    rounds_to_win = 3

    # Start Game
    ui.display_menu()

    #  Validate the round
    while game.validate_round(round_number, max_rounds, pc_score, user_score, rounds_to_win):
        # Get the user choice
        user_choice = ui.get_user_choice()

        # Validate user choice
        while not game.validate_user_choice(user_choice):
            ui.get_error_message('Invalid option. try again.')
            user_choice = ui.get_user_choice()

        # Get the pc choice
        pc_choice = game.get_pc_choice()
        # Determine a winner for the round
        round_number, user_score, pc_score, winner = game.determine_winner(
            round_number, user_score, pc_score, user_choice, pc_choice)
        # Get round winner message
        message = ui.get_result_message(
            winner, user_choice, pc_choice, round_number)

    # Validate scores
    while game.validate_score(user_score, pc_score) == 'draw':
        # get draw message
        print(ui.draw_msg())
        # last game
        max_rounds += 1
        round_number, user_score, pc_score, winner = game.determine_winner(
            round_number, user_score, pc_score, user_choice, pc_choice)
        game.validate_score(user_score, pc_score)

    end_msg = ui.end_game_msg(game.validate_score(
        user_score, pc_score), round_number)
    print(end_msg)


if __name__ == '__main__':
    play_game()
