def print_board(board):
    print("-------------")
    for row in board:
        print("|", end=" ")
        for cell in row:
            print(cell, end=" | ")
        print("\n-------------")


def is_winner(board, player):
    for row in board:
        if row.count(player) == 3:
            return True

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True

    if board[0][0] == board[1][1] == board[2][2] == player:
        return True

    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False


def is_board_full(board):
    for row in board:
        if " " in row:
            return False
    return True


def play_game():
    board = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]

    current_player = "X"

    while True:
        print_board(board)
        row = int(input("Enter the row (0, 1, or 2): "))
        col = int(input("Enter the column (0, 1, or 2): "))

        if board[row][col] == " ":
            board[row][col] = current_player
            if is_winner(board, current_player):
                print_board(board)
                print("Player", current_player, "wins!")
                break
            elif is_board_full(board):
                print_board(board)
                print("It's a tie!")
                break
            else:
                current_player = "O" if current_player == "X" else "X"
        else:
            print("Invalid move. Try again.")


print("Welcome to Tic Tac Toe!")
play_game()
