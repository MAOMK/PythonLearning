# Rock vs Paper vs Scissors
import get_messages
import game_utils as game

# Start the game
def start_game ():
    user_score = 0
    pc_score = 0
    round_number = 0    
    # Define rounds -> Global Scope
    max_rounds = 5
    # Define score to win
    rounds_to_win = 3
    # Start Game
    print(get_messages.gretting())
    # # Validate the round
    while game.validate_round(round_number , max_rounds, pc_score, user_score, rounds_to_win):        
        # Start a new round 
        round_number, user_score, pc_score = game.start_new_round(round_number, user_score, pc_score)

    # validate score
    while game.validate_score(user_score, pc_score) == 'draw':
        # get draw message
        print(get_messages.draw_msg())
        # last game
        max_rounds += 1
        round_number, user_score, pc_score = game.start_new_round(max_rounds, user_score, pc_score)
        game.validate_score(user_score, pc_score)
    
    end_msg = get_messages.end_game_msg(game.validate_score(user_score, pc_score), round_number)    
    print(end_msg)
            

if __name__ == '__main__':
    start_game()
