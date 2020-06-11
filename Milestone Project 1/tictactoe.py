"""

Play tic tac toe with a friend

"""


tic_tact_toe = {
    "upper_left": " ",
    "upper_middle": " ",
    "upper_right": " ",
    "middle_left": " ",
    "middle_middle": " ",
    "middle_right": " ",
    "bottom_left": " ",
    "bottom_middle": " ",
    "bottom_right": " ",
}

player_piece = {
    "player1": "",
    "player2": "",
}


def display_board():
    print(f'{tic_tact_toe["upper_left"]} | {tic_tact_toe["upper_middle"]} | {tic_tact_toe["upper_right"]}')
    print('-' * 10)
    print(f'{tic_tact_toe["middle_left"]} | {tic_tact_toe["middle_middle"]} | {tic_tact_toe["middle_right"]}')
    print('-' * 10)
    print(f'{tic_tact_toe["bottom_left"]} | {tic_tact_toe["bottom_middle"]} | {tic_tact_toe["bottom_right"]}')


def user_piece_choice(player):
    valid_inputs = ["x", "o"]

    choice = input(f"Please Choose X or O for {player}")
    if choice.lower() in valid_inputs:
        if choice.lower() == "x":
            player_piece["player1"] = choice.upper()
            player_piece["player2"] = "O"
            return True
        else:
            player_piece["player1"] = choice.upper()
            player_piece["player2"] = "X"
            return True
    else:
        print("Please Choose X or O")
    return False


def choose_move(player, valid_choice=False):
    if valid_choice:
        player_choice = input(f"{player}, Which square would you like to play? 1-9: ")
        try:
            player_choice = int(player_choice)
        except:
            print("Please enter a number 1-9")

        if player_choice in range(1, 10):
            if update_board(player, player_choice):
                return True
            else:
                return False


def update_board(player, choice):
    choices = {
        1: "upper_left",
        2: "upper_middle",
        3: "upper_right",
        4: "middle_left",
        5: "middle_middle",
        6: "middle_right",
        7: "bottom_left",
        8: "bottom_middle",
        9: "bottom_right",
    }
    if len(tic_tact_toe[choices[choice]]) != 1:
        tic_tact_toe[choices[choice]] = player_piece[player]
        return True
    else:
        return False


def check_winner():
    if len(set(tic_tact_toe["upper_left"], tic_tact_toe["middle_left"], tic_tact_toe["bottom_left"])) == 1:
        return tic_tact_toe["upper_left"], True
    elif len(set(tic_tact_toe["upper_middle"], tic_tact_toe["middle_middle"], tic_tact_toe["bottom_middle"])) == 1:
        return tic_tact_toe["upper_middle"], True
    elif len(set(tic_tact_toe["upper_right"], tic_tact_toe["middle_right"], tic_tact_toe["bottom_right"])) == 1:
        return tic_tact_toe["upper_right"], True
    elif len(set(tic_tact_toe["upper_left"], tic_tact_toe["upper_middle"], tic_tact_toe["upper_right"])) == 1:
        return tic_tact_toe["upper_left"], True
    elif len(set(tic_tact_toe["middle_left"], tic_tact_toe["middle_middle"], tic_tact_toe["middle_right"])) == 1:
        return tic_tact_toe["middle_left"], True
    elif len(set(tic_tact_toe["bottom_left"], tic_tact_toe["bottom_middle"], tic_tact_toe["bottom_right"])) == 1:
        return tic_tact_toe["bottom_left"], True
    elif len(set(tic_tact_toe["bottom_left"], tic_tact_toe["middle_middle"], tic_tact_toe["upper_right"])) == 1:
        return tic_tact_toe["upper_left"], True
    elif len(set(tic_tact_toe["bottom_right"], tic_tact_toe["middle_middle"], tic_tact_toe["upper_left"])) == 1:
        return tic_tact_toe["bottom_right"], True

print("Welcome to Tic-Tac-Toe")
# choice = user_piece_choice()

# count = 1
# for item in tic_tact_toe.keys():
#     print(f'{count}:"{item}",')
#     count += 1
player_piece["player1"] = "X"

check_winner()