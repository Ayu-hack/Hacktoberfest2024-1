// Problem statement
// For a given two-dimensional integer array/list of size (N x M), you need to find out which row or column has the largest sum(sum of all the elements in a row or column) amongst all the rows/columns.

// Note :
// If there are more than one rows/columns with maximum sum, consider the row/column that comes first. And if ith row and jth column has the same largest sum, consider the ith row as answer.
// Detailed explanation ( Input/output format, Notes, Images )
// Constraints:
// 1 <= t <= 10^2
// 1 <= N <= 10^3
// 1 <= M <= 10^3
// Time Limit: 1sec
// Sample Input 1:
// 1
// 3 2
// 6 9
// 8 5
// 9 2
// Sample Output 1:
// column 0 23
// Sample Input 2:
// 1
// 4 4
// 6 9 8 5
// 9 2 4 1
// 8 3 9 3
// 8 7 8 6
// Sample Output 2:
// column 0 31

// C++
#include <iostream>
#include <vector>
#include <limits>
using namespace std;

void findLargest(const vector<vector<int>> &input)
{
	try
	{
		int rows = input.size();
		int columns = input[0].size();
		int largest = numeric_limits<int>::min();
		int x = 0;
		int sum1 = 0;
		int sum2 = 0;
		string s = "";

		for (int i = 0; i < rows; i++)
		{
			sum1 = 0;
			for (int j = 0; j < columns; j++)
			{
				sum1 += input[i][j];
			}
			if (sum1 > largest)
			{
				largest = sum1;
				x = i;
				s = "row";
			}
		}
		for (int i = 0; i < columns; i++)
		{
			sum2 = 0;
			for (int j = 0; j < rows; j++)
			{
				sum2 += input[j][i];
			}
			if (sum2 > largest)
			{
				largest = sum2;
				x = i;
				s = "column";
			}
		}
		cout << s << " " << x << " " << largest << endl;
	}
	catch (const out_of_range &e)
	{
		cout << "row 0 -2147483648" << endl;
	}
}

int main()
{
	vector<vector<int>> input = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
	findLargest(input);
	return 0;
}

// Java
// public class Solution {
// 	public static void findLargest(int input[][]){
//      try{
//         int rows = input.length;
//         int columns = input[0].length;
//         int largest = Integer.MIN_VALUE;
//         int x = 0;
//         int sum1 = 0;
//         int sum2 = 0;
//         String s = "";

//            for(int i=0;i<rows;i++) {
//             sum1 = 0;
//             int j = 0;
//             for(;j<columns;j++) {
//                 sum1 += input[i][j];
//             }
//             if(sum1>largest) {
//                 largest = sum1;
//                 x = i;
//                 s = "row";
//             }
//         }
//         for(int i=0;i<columns-1;i++) {
//             sum2 = 0;
//             int j = 0;
//             for(;j<rows;j++) {
//                 sum2 += input[j][i];
//             }
//             if(sum2>largest) {
//                 largest = sum2;
//                 x = i;
//                 s = "column";
//             }
//         }
//     System.out.println(s + " " + x + " " + largest);
//         }

//         catch (ArrayIndexOutOfBoundsException e){
//             System.out.print("row 0 -2147483648" );
//         }
//     }
// }