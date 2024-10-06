#include <bits/stdc++.h>
using namespace std;
// https://www.interviewbit.com/problems/allocate-books/

// Helper function to check if we can allocate books such that no student gets more than 'mid' pages
bool isPoss(vector<int> &a, int b, int mid)
{
    int cnt = 1; // Start with one student
    int m = 0;   // Accumulate the pages for the current student

    // Traverse through each book
    for (int i = 0; i < a.size(); i++)
    {
        if (m + a[i] <= mid)
        { // If adding this book's pages doesn't exceed 'mid', allocate to current student
            m += a[i];
        }
        else
        {             // Otherwise, allocate the next book to a new student
            cnt++;    // Increase student count
            m = a[i]; // This book starts a new student's allocation
        }
    }

    // If the number of students is within the allowed number, return true
    return cnt <= b;
}

// Main function to allocate books
int booksAllocate(vector<int> &A, int B)
{
    // If there are more students than books, allocation is impossible
    if (B > A.size())
    {
        return -1;
    }

    int lo = 0; // Minimum possible pages to allocate
    int hi = 0; // Maximum possible pages to allocate (sum of all pages)

    // Find initial values for lo and hi
    for (int i = 0; i < A.size(); i++)
    {
        lo = max(lo, A[i]); // Minimum should at least be the largest book
        hi += A[i];         // Maximum is the sum of all pages
    }

    int ans = 0; // Store the final answer
    // Perform binary search between lo and hi
    while (lo <= hi)
    {
        int mid = lo + (hi - lo) / 2; // Find the middle point (possible max pages a student gets)
        if (isPoss(A, B, mid))
        {                 // Check if allocation is possible with 'mid' as the max
            ans = mid;    // If yes, save the result
            hi = mid - 1; // Try for a smaller maximum (minimize further)
        }
        else
        {
            lo = mid + 1; // If not possible, increase the minimum limit
        }
    }
    return ans; // Return the smallest possible maximum pages a student gets
}

int main()
{
    vector<int> A = {12, 34, 67, 90}; // Example input
    int B = 2;                        // Number of students
    cout << booksAllocate(A, B);      // Should output 113 (minimum of maximum pages)
    return 0;
}
