# Rock vs Paper vs Sissors

import random

horizontal_line = '*' * 10

# Create a Welcome Message
def gretting ():
    welcome_str = ' WELCOME TO ROCK, PAPER AND scissors' 
    return f"{horizontal_line} {welcome_str} {horizontal_line}"

# get the options to compare
def get_options ():
    # Define options for the pc
    pc_options = ('rock', 'paper', 'scissors')
    user_selection = input('rock, paper or scissors, make your choose: ')
    pc_selection = random.choice(pc_options)
    # normalize the options
    user_selection = user_selection.lower()
    return user_selection, pc_selection

def get_result_msg (user_selection = '', pc_selection = '', result = '', round_number = 0):
    text_a = f"{horizontal_line} {round_number} {horizontal_line}"
    text_b = f"user selection => {user_selection}"
    text_c = f"pc selection => {pc_selection}"
    text_d = f"{horizontal_line} {result.upper()} {horizontal_line}"
    return text_a, text_b, text_c, text_d

def get_winner_msg (winner, user_score, pc_score):
    # print('winner inside -> ', winner)
    if winner == 'user':
        user_score += 1
        message = 'you win'
        # print('entro acá')
    elif winner == 'pc':
        pc_score += 1
        message = 'you lose'
        # print('entro acá o acá')
    elif winner == 'draw':
        message = 'draw'  
        # print('entro acáaaaa') 
    return(message, user_score, pc_score)

def define_winner (user_selection, pc_selection):
    # define draw option
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
    else:
        round_number -=1
        print('no es una opción valida')
        return False    
    return winner

def validate_round (round_number, max_rounds, pc_score, user_score, rounds_to_win):
    # print('round_number -> ', round_number)
    # print('max_rounds -> ', max_rounds)
    # print('pc_score -> ', pc_score)
    # print('user_score -> ', user_score)
    # print('rounds_to_win -> ', rounds_to_win)
    playing = True
    if round_number == max_rounds or pc_score == rounds_to_win or user_score == rounds_to_win:
        playing = False
    else:
        playing = True
    # print('playing -> ', playing)
    return playing
    
def end_game_msg (winner, round_number):
    if winner == 'user':
        return f"{horizontal_line} GANASTE en {round_number} {horizontal_line}"
    else: 
        return f"{horizontal_line} PERDISTE en {round_number} {horizontal_line}"

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
    print(gretting())
    # Validate the round
    while validate_round(round_number , max_rounds, pc_score, user_score, rounds_to_win):        
        # Start a new round 
        round_number +=1
        # print('round_number +1 -> ', round_number)
        # get options
        user_selection, pc_selection = get_options()
        # print('user_selection -> ', user_selection)
        # print('pc_selection -> ', pc_selection)
        # define a round winner
        winner = define_winner(user_selection, pc_selection)
        # print('winner -> ', winner)
        # get round winner mesagge
        message , user_score, pc_score = get_winner_msg(winner, user_score, pc_score)
        # print('user_score -> ', user_score)
        # print('pc_score -> ', pc_score)
        # get round result mesagges
        text_a, text_b, text_c, text_d = get_result_msg(user_selection, pc_selection, message, round_number)
        print(text_a)
        print(text_b)
        print(text_c)
        print(text_d)
       
    end_msg = end_game_msg(winner, round_number)
    print(end_msg)
            


start_game()