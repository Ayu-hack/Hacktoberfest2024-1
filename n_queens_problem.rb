#solve the N-Queens problem in Ruby programming language.

# The N-Queens problem is the problem of placing N chess queens on an N×N chessboard
# so that no two queens threaten each other. Thus, a solution requires that no two
# queens share the same row, column, or diagonal.
# The function takes an integer N as input and returns a list of all valid solutions

# The function uses a recursive backtracking algorithm to find all possible solutions.

# Example:
# >>> n_queens_solver(4)
# Number of solutions for 4-Queens: 2
# Solution 1:
# . Q . .
# . . . Q
# Q . . .
# . . Q .
#
# Solution 2:
# . . Q .
# Q . . .
# . . . Q
# . Q . .

def n_queens_solver(n)
  solutions = []
  board = Array.new(n) { '.' * n }
  find_solutions(solutions, board, 0, n)
  solutions  
end

def find_solutions(solutions, board, row, n)
  if row == n
    solutions << board.map(&:dup)
    return
  end

  (0...n).each do |col|
    if can_place_queen?(board, row, col, n)
      board[row][col] = 'Q'
      find_solutions(solutions, board, row + 1, n)
      board[row][col] = '.'
    end
  end
end

def can_place_queen?(board, row, col, n)
  (0...row).each do |r|
    return false if board[r][col] == 'Q'
  end
  (1..row).each do |i|
    return false if row - i >= 0 && col - i >= 0 && board[row - i][col - i] == 'Q'
  end
  (1..row).each do |i|
    return false if row - i >= 0 && col + i < n && board[row - i][col + i] == 'Q'
  end
  true 
end

if __FILE__ == $PROGRAM_NAME
  print "Enter the size of the chessboard (n): "
  n = gets.to_i 
  result = n_queens_solver(n)
  puts "Number of solutions for #{n}-Queens: #{result.size}"
  result.each_with_index do |sol, idx|
    puts "Solution #{idx + 1}:"
    sol.each { |line| puts line }
    puts
  end
end