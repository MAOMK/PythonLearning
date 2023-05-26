# Rock vs Paper vs Siccors
import random

# Define options for the pc
pc_options = ('rock', 'paper', 'sissors')

# Define rounds
max_rounds = 5
rounds_to_win = 3
user_score = 0
pc_score = 0
playing = True
round_number = 0

# Create a Welcome Message
welcome_str = 'WELCOME TO ROCK, PAPER AND SISSORS'
print('*'*20, welcome_str, '*'*20,)

# Start the game
while playing:
    # get the options to compare
    user_selection = input('rock, paper or sissors, make your choose: ')
    pc_selection = random.choice(pc_options)
    round_number +=1
    # normalize the options
    user_selection = user_selection.lower()
    # define draw option
    if( user_selection == pc_selection ):
        print('+'*10, ' Round #', round_number, '+'*10)
        print('pc selection => ', pc_selection)
        print('Draw!!!')
    # define actions for user_selection == paper
    elif( user_selection == 'paper' ):
        # paper vs rock -> paper wins
        if(pc_selection == 'rock'):
            print('+'*10, ' Round #', round_number, '+'*10)
            print('pc selection => ', pc_selection)
            print('You Win!!!')
            user_score += 1
        # paper vs sissors -> sissors wins
        if(pc_selection == 'sissors'):
            print('+'*10, ' Round #', round_number, '+'*10)
            print('pc selection => ', pc_selection)
            print('You Lose!!!')
            pc_score += 1
    # define actions for user_selection == sissors
    elif( user_selection == 'sissors' ):
        # sissors vs rock -> rock wins
        if(pc_selection == 'rock'):
            print('+'*10, ' Round #', round_number, '+'*10,)
            print('pc selection => ', pc_selection)
            print('You Lose!!!')
            pc_score += 1
        # sissors vs paper -> sissors wins
        if(pc_selection == 'paper'):
            print('+'*10, ' Round #', round_number, '+'*10)
            print('pc selection => ', pc_selection)
            print('You win!!!')
            user_score += 1
    # define actions for user_selection == rock
    elif( user_selection == 'rock' ):
        # rock vs sissors -> rock wins
        if(pc_selection == 'sissors'):
            print('+'*10, ' Round #', round_number, '+'*10)
            print('pc selection => ', pc_selection)
            print('You win!!!')
            user_score += 1
        # rock vs paper -> paper wins
        if(pc_selection == 'paper'):
            print('+'*10, ' Round #', round_number, '+'*10)
            print('pc selection => ', pc_selection)
            print('You Lose!!!')
            pc_score += 1
    else:
        round_number -=1
        print('no es una opción valida')
    # define a winner
    if pc_score == 3 or user_score == 3 or round_number == max_rounds:
        playing = False
        continue
# END game
if user_score == 3:
    print('*'*20, 'GANASTE en ', round_number, ' rondas', '*'*20)
else:
    print('*'*20, 'PERDISTE en ', round_number, ' rondas', '*'*20)