separator = '*' * 10

# Create a Welcome message
def gretting ():
    welcome_str = ' WELCOME TO ROCK, PAPER AND SCISSORS' 
    return f"{separator} {welcome_str} {separator}"

# Create a Draw message
def draw_msg ():
    welcome_str = ' DRAW!!! SHAN SHAN SHAN!!!! FINAL ROUND:' 
    return f"{separator} {welcome_str} {separator}"

# Get a message for the end of each round
def get_result_msg (user_selection = '', pc_selection = '', result = '', round_number = 0):
    text_a = f"{separator} {round_number} {separator}"
    text_b = f"user selection => {user_selection}"
    text_c = f"pc selection => {pc_selection}"
    text_d = f"{separator} {result.upper()} {separator}"
    return text_a, text_b, text_c, text_d

def end_game_msg (winner, round_number):
    print('winnner--> ', winner)
    if winner == 'user':
        return f"{separator} GANASTE en {round_number} {separator}"
    else: 
        return f"{separator} PERDISTE en {round_number} {separator}"