public class SudokoSolver {

    static int count = 0;
    public static boolean isSafe(int board[][],int row,int col,int digit){

        //condiron check for column:
        for(int i=0;i<9;i++){
            if(board[row][i]==digit){
                return false;
            }
        }

        //condition check for row:
        for(int i=0;i<9;i++){
            if(board[i][col]==digit){
                return false;
            }
        }


        //Inside same grid:
        int sr = (row/3) * 3;
        int sc = (col/3) * 3;

        for(int i=sr;i<sr+3;i++){
            for(int j=sc;j<sc+3;j++){
                if(board[i][j]==digit){
                    return false;
                }
            }
        }
           
        return true;
    }

    public static boolean sudokuSolver(int board[][],int row,int col){
        if(row == 9){
            count++;
            return true;
        }

        int nextRow = row, nextCol = col+1;
        if(col+1 == 9){
           nextRow = row+1;
           nextCol = 0;
        }

        if(board[row][col] != 0){
            return sudokuSolver(board,nextRow,nextCol);
        }

        for(int digit=1;digit<=9;digit++){
            if(isSafe(board,row,col,digit)){
                board[row][col] = digit;
                if(sudokuSolver(board, nextRow, nextCol)){
                    return true;
                }
                board[row][col] = 0;
            }
        }
        return false;
    }


    public static void printBoard(int board[][]){
        for(int i=0;i<9;i++){
            for(int j=0;j<9;j++){
                System.out.print(board[i][j]+" ");
            }
            System.out.println();
        }
    }

    public static void main(String[] args) {
        int[][] board = {{0,0,8,0,0,0,0,0,0},
                         {4,9,0,1,5,7,0,0,2},
                         {0,0,3,0,0,4,1,9,0},
                         {1,8,5,0,6,0,0,2,0},
                         {0,0,0,0,2,0,0,6,0},
                         {9,6,0,4,0,5,3,0,0},
                         {0,3,0,0,7,2,0,0,4},
                         {0,4,9,0,3,0,0,5,7},
                         {8,2,7,0,0,9,0,1,3}};
        
        if(sudokuSolver(board, 0, 0)){
            System.out.println("Solution Exists");
            System.out.println("There are total :"+ count);
            printBoard(board);
        }else{
            System.out.println("Solution does not existf");
        }
    }
}
