#include <iostream>
using namespace std;
int fibonacciRec(int n) {
    if (n <= 1) {
        return n;
    }
    return fibonacciRec(n - 1) + fibonacciRec(n - 2);
}
void fibonacciIter(int terms) {
    int a = 0, b = 1, next;
    cout << "Fibonacci Series: " << a << ", " << b;
    for (int i = 2; i < terms; i++) {
        next = a + b;
        cout << ", " << next;
        a = b;
        b = next;
    }
    cout << endl;
}
int main() {
    int choice, n;
    cout << "Choose an option:\n";
    cout << "1. Fibonacci number at a specific position\n";
    cout << "2. Generate Fibonacci series up to a certain number of terms\n";
    cin >> choice;
    switch (choice) {
        case 1:
            cout << "Enter the position (0-indexed) of the Fibonacci number: ";
            cin >> n;
            cout << "Fibonacci number at position " << n << " is: " << fibonacciRec(n) << endl;
            break;
        case 2:
            cout << "Enter the number of terms: ";
            cin >> n;
            fibonacciIter(n);
            break;
        default:
            cout << "Invalid choice!" << endl;
            break;
    }
    return 0;
}
