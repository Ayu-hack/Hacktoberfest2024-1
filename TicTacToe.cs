using System;

class TicTacToe
{
    static char[] board = new char[9] { ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ' };

    static void DisplayBoard()
    {
        Console.WriteLine($"{board[0]} | {board[1]} | {board[2]}");
        Console.WriteLine("--|---|--");
        Console.WriteLine($"{board[3]} | {board[4]} | {board[5]}");
        Console.WriteLine("--|---|--");
        Console.WriteLine($"{board[6]} | {board[7]} | {board[8]}");
    }

    static bool IsGameOver()
    {
        for (int i = 0; i < 9; i += 3)
        {
            if (board[i] == board[i + 1] && board[i + 1] == board[i + 2] && board[i] != ' ')
                return true;
        }

        for (int i = 0; i < 3; i++)
        {
            if (board[i] == board[i + 3] && board[i + 3] == board[i + 6] && board[i] != ' ')
                return true;
        }

        if (board[0] == board[4] && board[4] == board[8] && board[0] != ' ')
            return true;
        if (board[2] == board[4] && board[4] == board[6] && board[2] != ' ')
            return true;

        if (Array.IndexOf(board, ' ') == -1)
            return true;

        return false;
    }

    static int GetPlayerInput(char player)
    {
        while (true)
        {
            Console.Write($"Player {player}, enter your position (1-9): ");
            string input = Console.ReadLine();
            if (int.TryParse(input, out int position) && position >= 1 && position <= 9 && board[position - 1] == ' ')
                return position - 1;
            else
                Console.WriteLine("Invalid input. Please try again.");
        }
    }

    static void Main()
    {
        char currentPlayer = 'X';
        while (!IsGameOver())
        {
            DisplayBoard();
            int position = GetPlayerInput(currentPlayer);
            board[position] = currentPlayer;
            currentPlayer = currentPlayer == 'X' ? 'O' : 'X';
        }

        DisplayBoard();
        if (Array.IndexOf(board, ' ') == -1)
            Console.WriteLine("It's a tie!");
        else
            Console.WriteLine($"Player {(currentPlayer == 'X' ? 'O' : 'X')} wins!");
    }
}