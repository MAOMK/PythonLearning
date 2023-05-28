separator = '*' * 10
options = ('rock', 'paper', 'scissors')


# Create a Welcome message
def display_menu():
    welcome_str = """
        Welcome to Rock, Paper, Scissors!
        ╔═══════════════════════════╗
        ║     📜 Game Rules         ║
        ╟───────────────────────────╢
        ║  - The first player to    ║
        ║    win three rounds wins  ║
        ║    the game.              ║
        ║  - If there is a tie      ║
        ║    after five rounds, a   ║
        ║    sudden death round     ║
        ║    will be played.        ║
        ║  - In sudden death, the   ║
        ║    first player to win a  ║
        ║    round wins the game.   ║
        ╟───────────────────────────╢
        ║     🎮  Options           ║
        ╟───────────────────────────╢
        ║          Rock             ║
        ║          Paper            ║
        ║          Scissors         ║
        ╚═══════════════════════════╝
    """
    print(welcome_str)


def get_user_choice():
    # Define options for the pc
    # Get the user choice
    user_selection = input('Enter your choice: ')
    # normalize the options
    user_selection = user_selection.lower()
    return user_selection


def get_error_message(error):
    error_message = f"""
            ERROR
        --------------
        {error}
    """
    print(error_message)


def get_result_message(winner, user_choice, pc_choice, round_number):
    # get round winner message
    if winner == 'user':
        message = 'you win'
    elif winner == 'pc':
        message = 'you lose'
    elif winner == 'draw':
        message = 'draw'
    # Print round result messages
    round_message = f"""
    ╔═══════════════════════╗
    ║     Round Result      ║
    ╟───────────────────────╢
    ║ Round number:  {round_number}      ║
    ║ User choice: {user_choice} ║
    ║ Pc choice:  {pc_choice}      ║
    ╟───────────────────────╢
    ║       {message}        ║
    ╟───────────────────────╢
    ║       Next round ->   ║
    ╚═══════════════════════╝
    """
    print(round_message)


# Create a Draw message
def draw_msg():
    welcome_str = ' DRAW!!! SHAN SHAN SHAN!!!! FINAL ROUND:'
    return f"{separator} {welcome_str} {separator}"


def end_game_msg(winner, round_number):
    if winner == 'user':
        return f"{separator} GANASTE en {round_number} {separator}"
    else:
        return f"{separator} PERDISTE en {round_number} {separator}"
