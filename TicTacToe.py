# Tic-Tac-Toe Game

# Constants for players
PLAYER_X = "X"
PLAYER_O = "O"
EMPTY = " "
board = [EMPTY for _ in range(9)]

def display_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--|---|--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--|---|--")
    print(f"{board[6]} | {board[7]} | {board[8]}")

def is_game_over(board):
    winning_positions = [
        # Horizontal
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        # Vertical
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        # Diagonal
        (0, 4, 8), (2, 4, 6)
    ]
    
    for a, b, c in winning_positions:
        if board[a] == board[b] == board[c] != EMPTY:
            return True
            
    return EMPTY not in board  # Check for tie if no winner

def get_player_input(player):
    while True:
        position = input(f"Player {player}, enter your position (1-9): ")
        if position.isdigit() and 1 <= int(position) <= 9:
            index = int(position) - 1
            if board[index] == EMPTY:
                return index
            else:
                print("Position already taken. Please try again.")
        else:
            print("Invalid input. Please try again.")

def play_game():
    current_player = PLAYER_X
    while not is_game_over(board):
        display_board(board)
        position = get_player_input(current_player)
        board[position] = current_player
        current_player = PLAYER_O if current_player == PLAYER_X else PLAYER_X

    display_board(board)
    if EMPTY not in board:
        print("It's a tie!")
    else:
        winner = "Player X" if current_player == PLAYER_O else "Player O"
        print(f"{winner} wins!")

if __name__ == "__main__":
    play_game()
