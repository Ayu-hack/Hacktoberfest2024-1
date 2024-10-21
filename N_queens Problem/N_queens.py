def print_solution(board):
    """Helper function to print the board configuration."""
    for row in board:
        print(" ".join("Q" if x else "." for x in row))
    print()

def is_safe(board, row, col):
    """Check if it's safe to place a queen at board[row][col]."""
    # Check this column on upper side
    for i in range(row):
        if board[i][col]:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if j < 0:
            break
        if board[i][j]:
            return False

    # Check upper diagonal on right side
    for i, j in zip(range(row, -1, -1), range(col, len(board))):
        if j >= len(board):
            break
        if board[i][j]:
            return False

    return True

def solve_n_queens_util(board, row):
    """Utilizes backtracking to solve the N-Queens problem."""
    if row >= len(board):
        print_solution(board)
        return True

    res = False
    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row][col] = True  # Place the queen
            res = solve_n_queens_util(board, row + 1) or res
            board[row][col] = False  # Backtrack

    return res

def solve_n_queens(n):
    """Main function to solve the N-Queens problem."""
    board = [[False for _ in range(n)] for _ in range(n)]
    if not solve_n_queens_util(board, 0):
        print("Solution does not exist")
    return

# Example usage
n = 4
solve_n_queens(n)
