import random
import ui as ui

options = ('rock', 'paper', 'scissors')


# Validate user selection
def validate_user_choice (user_choice):    
    if user_choice not in options:
        return False
    else:
        return True

# Get pc random choose
def get_pc_choice ():
    pc_choice = random.choice(options)  
    return pc_choice

def determine_winner (round_number, user_score, pc_score, user_choice, pc_choice):
    # start a new round
    round_number +=1
    # define a round winner
    if user_choice == pc_choice :
        winner = 'draw'
    # define actions for user_choice wins
    elif (
        (user_choice == 'paper' and pc_choice == 'rock') or
        (user_choice == 'scissors' and pc_choice == 'paper') or
        (user_choice == 'rock' and pc_choice == 'scissors')
    ):
        winner = 'user'
        user_score += 1            
    else:
        winner = 'pc'
        pc_score += 1    
    return(round_number, user_score, pc_score, winner)


def validate_round (round_number, max_rounds, user_score, pc_score, rounds_to_win):
    if (
        round_number == max_rounds or 
        pc_score == rounds_to_win or 
        user_score == rounds_to_win
    ):
        return False
    else:
        return True

def validate_score(user_score, pc_score):
    if pc_score == user_score:
        winner = 'draw'
    elif user_score > pc_score:
        winner = 'user'
    else:
        winner = 'pc'
    return winner
