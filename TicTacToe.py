# Tic-Tac-Toe Game


board = [" " for _ in range(9)]


def display_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--|---|--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--|---|--")
    print(f"{board[6]} | {board[7]} | {board[8]}")


def is_game_over(board):

    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2] != " ":
            return True
    
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] != " ":
            return True
    
    if board[0] == board[4] == board[8] != " ":
        return True
    if board[2] == board[4] == board[6] != " ":
        return True
    
    if " " not in board:
        return True
    return False


def get_player_input(player):
    while True:
        position = input(f"Player {player}, enter your position (1-9): ")
        if position.isdigit() and 1 <= int(position) <= 9 and board[int(position) - 1] == " ":
            return int(position) - 1
        else:
            print("Invalid input. Please try again.")


current_player = "X"
while not is_game_over(board):
    display_board(board)
    position = get_player_input(current_player)
    board[position] = current_player
    current_player = "O" if current_player == "X" else "X"

display_board(board)
if " " not in board:
    print("It's a tie!")
else:
    winner = "Player X" if current_player == "O" else "Player O"
    print(f"{winner} wins!")

