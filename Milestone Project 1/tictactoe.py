"""

Play tic tac toe with a friend

"""

tic_tac_toe_board = {
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
    print(
        f'{tic_tac_toe_board["upper_left"]} | {tic_tac_toe_board["upper_middle"]} | {tic_tac_toe_board["upper_right"]}')
    print('-' * 10)
    print(
        f'{tic_tac_toe_board["middle_left"]} | {tic_tac_toe_board["middle_middle"]} | '
        f'{tic_tac_toe_board["middle_right"]}')
    print('-' * 10)
    print(
        f'{tic_tac_toe_board["bottom_left"]} | {tic_tac_toe_board["bottom_middle"]} | '
        f'{tic_tac_toe_board["bottom_right"]}')


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
    if tic_tac_toe_board[choices[choice]] == " ":
        tic_tac_toe_board[choices[choice]] = player_piece[player]
        return True
    else:
        return False


def check_winner():
    if tic_tac_toe_board["upper_left"] == tic_tac_toe_board["middle_left"] == tic_tac_toe_board["bottom_left"] != " ":
        return [tic_tac_toe_board["upper_left"], True]
    elif tic_tac_toe_board["upper_middle"] == tic_tac_toe_board["middle_middle"] == tic_tac_toe_board[
        "bottom_middle"] != " ":
        return [tic_tac_toe_board["upper_middle"], True]
    elif tic_tac_toe_board["upper_right"] == tic_tac_toe_board["middle_right"] == tic_tac_toe_board[
        "bottom_right"] != " ":
        return [tic_tac_toe_board["upper_right"], True]
    elif tic_tac_toe_board["upper_left"] == tic_tac_toe_board["upper_middle"] == tic_tac_toe_board[
        "upper_right"] != " ":
        return [tic_tac_toe_board["upper_left"], True]
    elif tic_tac_toe_board["middle_left"] == tic_tac_toe_board["middle_middle"] == tic_tac_toe_board[
        "middle_right"] != " ":
        return [tic_tac_toe_board["middle_left"], True]
    elif tic_tac_toe_board["bottom_left"] == tic_tac_toe_board["bottom_middle"] == tic_tac_toe_board[
        "bottom_right"] != " ":
        return [tic_tac_toe_board["bottom_left"], True]
    elif tic_tac_toe_board["bottom_left"] == tic_tac_toe_board["middle_middle"] == tic_tac_toe_board[
        "upper_right"] != " ":
        return [tic_tac_toe_board["bottom_left"], True]
    elif tic_tac_toe_board["bottom_right"] == tic_tac_toe_board["middle_middle"] == tic_tac_toe_board[
        "upper_left"] != " ":
        return [tic_tac_toe_board["bottom_right"], True]
    else:
        return [False, False]


def user_piece_choice(player):
    valid_inputs = ["x", "o"]

    choice = input(f"Please Choose X or O for {player}: ")
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
            return update_board(player, player_choice)


def clear_board_display():
    print("\n" * 30)


def get_key(player_piece_choice):
    for key, value in player_piece.items():
        if value == player_piece_choice:
            return key


def display_winner(player):
    player = get_key(player)
    if winner:
        clear_board_display()
        print(f'{player} has won the game!')
        display_board()
        return True

    return False


def check_for_full_board():
    count = 0
    for value in tic_tac_toe_board.values():
        if value != " ":
            count += 1

    if count == 9:
        print("No Winner!")
        return True
    else:
        return False


print("Welcome to Tic-Tac-Toe")

display_board()

while True:
    player, winner = check_winner()
    if winner:
        display_winner(player)
        break

    if check_for_full_board():
        break

    valid_input = user_piece_choice("player1")
    if valid_input:
        while True:
            player, winner = check_winner()

            if check_for_full_board():
                break

            if winner:
                break

            player1_valid = choose_move("player1", True)

            if player1_valid:
                display_board()

                while True:
                    player, winner = check_winner()

                    if check_for_full_board():
                        break

                    if winner:
                        break

                    player2_valid = choose_move("player2", True)

                    if player2_valid:
                        display_board()
                        break
                    else:
                        print("Please choose a valid Square!")
                        continue
            else:
                print("Please choose a valid Square!")
                continue
