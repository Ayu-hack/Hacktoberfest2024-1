#include <iostream>
#include <algorithm> // For std::min

// Function to calculate GCD using brute force approach
int calculateGCD_BruteForce(int firstNumber, int secondNumber) {
    int greatestCommonDivisor = 1;

    for (int i = 1; i <= std::min(firstNumber, secondNumber); i++) {
        if (firstNumber % i == 0 && secondNumber % i == 0) {
            greatestCommonDivisor = i;
        }
    }

    return greatestCommonDivisor;
}

// Function to calculate GCD using Euclidean algorithm
int calculateGCD_Euclidean(int firstNumber, int secondNumber) {
    while (secondNumber != 0) {
        int temp = secondNumber;
        secondNumber = firstNumber % secondNumber;
        firstNumber = temp;
    }
    return firstNumber;
}

// Function to calculate GCD using Binary GCD (Stein's Algorithm)
int calculateGCD_Binary(int firstNumber, int secondNumber) {
    if (firstNumber == 0) return secondNumber;
    if (secondNumber == 0) return firstNumber;

    // Find the number of common factors of 2
    int shift;
    for (shift = 0; ((firstNumber | secondNumber) & 1) == 0; ++shift) {
        firstNumber >>= 1;
        secondNumber >>= 1;
    }
    
    // Make firstNumber odd
    while ((firstNumber & 1) == 0) {
        firstNumber >>= 1;
    }

    // Apply the binary GCD algorithm
    do {
        while ((secondNumber & 1) == 0) {
            secondNumber >>= 1;
        }

        if (firstNumber > secondNumber) {
            std::swap(firstNumber, secondNumber);
        }
        
        secondNumber -= firstNumber;
    } while (secondNumber != 0);

    return firstNumber << shift; // Restore the common factors of 2
}

int main() {
    int number1 = 36;
    int number2 = 60;

    std::cout << "Brute Force GCD: " << calculateGCD_BruteForce(number1, number2) << std::endl;
    std::cout << "Euclidean GCD: " << calculateGCD_Euclidean(number1, number2) << std::endl;
    std::cout << "Binary GCD: " << calculateGCD_Binary(number1, number2) << std::endl;

    return 0;
}
