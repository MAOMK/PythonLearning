import random
import get_messages

pc_options = ('rock', 'paper', 'scissors')


# get the options to compare
def get_selections ():
    # Define options for the pc
    # Get the user choose
    user_selection = input('rock, paper or scissors, make your choose: ')
    # Get pc random choose
    pc_selection = random.choice(pc_options)
    # normalize the options
    user_selection = user_selection.lower()
    return user_selection, pc_selection

def validate_selections (user_selection):
    return user_selection in pc_options

def define_winner (user_selection, pc_selection):
    # define actions for draw option
    if( user_selection == pc_selection ):
        winner = 'draw'
    # define actions for user_selection == paper
    elif( user_selection == 'paper' ):
        # paper vs rock -> paper wins
        if(pc_selection == 'rock'):
            winner = 'user'            
        # paper vs scissors -> scissors wins
        if(pc_selection == 'scissors'):
            winner = 'pc'
    # define actions for user_selection == scissors
    elif( user_selection == 'scissors' ):
        # scissors vs rock -> rock wins
        if(pc_selection == 'rock'):
            winner = 'pc'
        # scissors vs paper -> scissors wins
        if(pc_selection == 'paper'):
            winner = 'user'
    # define actions for user_selection == rock
    elif( user_selection == 'rock' ):
        # rock vs scissors -> rock wins
        if(pc_selection == 'scissors'):
            winner = 'user'
        # rock vs paper -> paper wins
        if(pc_selection == 'paper'):
            winner = 'pc'
    # define actions for incorrect selection
    else:
        winner = 'none'
    return winner

def get_round_result (winner, user_score, pc_score):
    if winner == 'user':
        user_score += 1
        message = 'you win'
    elif winner == 'pc':
        pc_score += 1
        message = 'you lose'
    elif winner == 'draw':
        message = 'draw'  
    elif winner == 'none':
        message = 'Invalid Option, try again.'
    return(message, user_score, pc_score)

def start_new_round (round_number, user_score, pc_score):
    # start a new round
    round_number +=1
    # get selections
    user_selection, pc_selection = get_selections()
    # validate user selection
    if validate_selections(user_selection):
        # define a round winner
        winner = define_winner(user_selection, pc_selection)
        # get round winner mesagge
        message , user_score, pc_score = get_round_result(winner, user_score, pc_score)
        # get round result mesagges
        text_a, text_b, text_c, text_d = get_messages.get_result_msg(user_selection, pc_selection, message, round_number)
        print(text_a)
        print(text_b)
        print(text_c)
        print(text_d)
    else:
        print('Invalid option, try again!!!')
        round_number -= 1
    return(round_number, user_score, pc_score)


def validate_round (round_number, max_rounds, user_score, pc_score, rounds_to_win):
    playing = True
    if round_number == max_rounds or pc_score == rounds_to_win or user_score == rounds_to_win:
        playing = False
    else:
        playing = True
    return playing

def validate_score(user_score, pc_score):
    if pc_score == user_score:
        winner = 'draw'
    elif user_score > pc_score:
        winner = 'user'
    else:
        winner = 'pc'
    return winner
