#!/usr/bin/python3

def sanitize_user_input(move: str) -> bool:
    """
    ACCEPTABLE user input is "R C". ROW SPACE COL. We have to ensure that this is what the user provides!


    :param: "move" str. The raw user input

    :returns: bool. True if everything is ok. False otherwise

    """

    def is_valid_char(char: str) -> bool:

        # ROW or COL char is NOT a digit.
        if not char.isdigit():
            return False

            # ROW or COL char is outside the boundaries of the board.
        if int(char) < 0 or int(char) > 2:
            return False

        return True

    if len(move) != 3:
        print("User input length != 3. Format is \"R C\".")
        return False

    if move[1] != ' ':
        print("User input character 2 HAS to be SPACE!")
        return False

    row = move[0]
    col = move[2]

    if not is_valid_char(row):
        print("ROW character is not in the correct format or is out-of-bounds")
        return False

    if not is_valid_char(col):
        print("COL character is not in the correct format or is out-of-bounds")
        return False

    return True


def get_user_input() -> str:
    user_move = input("Enter move: ")

    while sanitize_user_input(user_move) == False:
        user_move = input("Enter move: ")

    return user_move


def full(table: list, move: str) -> bool:
    """
    Checks whether a cell is occupied or not.

    :param: "table" list. The tic-tac-toe board
    :param: "move" str. The current user input in the format "r c" where r is row and c is column

    :returns" bool. True if cell is free/unocuppied. False otherwise
    """

    valid = True

    row, col = int(move[0]), int(move[1])

    if table[row][col] != '-':
        valid = False

    return valid


def print_tictactoe(table: list) -> None:
    print(" " * 8, "Col. 0 Col. 1 Col. 2")

    for i in range(len(table)):

        print("Row %d" % i, end='')

        for j in range(len(table[0])):
            print("%7s" % table[i][j], end='')

        print()


def check_won(table: list, turn: int) -> bool:
    """
    Checks whether one of the following conditions has been met
    1. a row is filled with the same character
    2. a col is filled with the same character
    3. a diag is filled iwth the same character

    :param: "table" list. The tic-tac-toe board
    :param: "turn" int. 1 if P1 2 if P2 is currently playing

    :returns: bool. True if either of the win conditions has been met. False otherwise.
    """

    checking_character = ""

    if turn == 1:
        checking_character = 'X'
    else:
        checking_character = 'O'

    # checking_character = 'X' if turn == 1 else 'O' # ternary if operator

    won = False

    # checking for rows
    for i in range(len(table)):

        if table[i][0] == checking_character and table[i][1] == checking_character and table[i][
            2] == checking_character:
            return True

    # checking for columns
    for j in range(len(table[0])):

        if table[0][j] == checking_character and table[1][j] == checking_character and table[2][
            j] == checking_character:
            return True

    # checking for 2 diags

    if (table[0][0] == checking_character and table[1][1] == checking_character and table[2][
        2] == checking_character) or \
            (table[0][2] == checking_character and table[1][1] == checking_character and table[2][
                0] == checking_character):
        return True

        # no win condition has been met (yet)
    return False


def check_over(table: list) -> bool:
    """
    Checks whether the game is over.

    :param: "table" list. The tic-tac-toe board

    :returns: bool. True if game is over, False otherwise.
    """

    for i in range(len(table)):

        for j in range(len(table[0])):

            if table[i][j] == "-":
                return False

    return True


def main():
    tictactoe = [
        ['-', '-', '-'],
        ['-', '-', '-'],
        ['-', '-', '-']
    ]
    print_tictactoe(tictactoe)

    turn = 1
    won = False
    over = False

    while not won and not over:

        if turn == 1:

            move_p1 = get_user_input()

            # Check whether current box is available
            valid = False
            while not valid:

                coordinates = move_p1.split()

                valid = full(tictactoe, coordinates)
                if not valid:
                    print("Selected box is already full try again")

                    move_p1 = get_user_input()

            tictactoe[int(coordinates[0])][int(coordinates[1])] = 'X'

            # Check TIE or WON for P1
            won = check_won(tictactoe, turn)
            if won:
                print("player 1 won!!")

            else:
                over = check_over(tictactoe)
                if over:
                    print("game ended in a tie")

            print_tictactoe(tictactoe)

            # Switch turns
            turn = 2


        else:

            move_p2 = get_user_input()

            # Check whether current box is available
            valid = False
            while not valid:

                coordinates = move_p2.split()

                valid = full(tictactoe, coordinates)
                if not valid:
                    print("Selected box is already full try again")

                    move_p2 = get_user_input()

            tictactoe[int(coordinates[0])][int(coordinates[1])] = 'O'

            # Check TIE or WON for P2
            won = check_won(tictactoe, turn)
            if won:
                print("player 2 won!!")

            else:
                over = check_over(tictactoe)
                if over:
                    print("game ended in a tie")

            print_tictactoe(tictactoe)

            # Switch turns
            turn = 1


if __name__ == "__main__":
    main()
