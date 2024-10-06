#include <iostream>
using namespace std;

// Ternary Search function for finding an element in a sorted array
int ternarySearch(int arr[], int l, int r, int key)
{
    while (r >= l)
    {
        // Divide the search space into 3 parts
        int mid1 = l + (r - l) / 3;
        int mid2 = r - (r - l) / 3;

        // Check if the key is at mid1 or mid2
        if (arr[mid1] == key)
        {
            return mid1; // Key found at mid1
        }
        if (arr[mid2] == key)
        {
            return mid2; // Key found at mid2
        }

        // Since the key is not present at mid1 or mid2,
        // we check in which part of the array it lies and discard the other two thirds.
        if (key < arr[mid1])
        {
            // Search in the left part
            r = mid1 - 1;
        }
        else if (key > arr[mid2])
        {
            // Search in the right part
            l = mid2 + 1;
        }
        else
        {
            // Search in the middle part
            l = mid1 + 1;
            r = mid2 - 1;
        }
    }
    // Key not found
    return -1;
}

int main()
{
    int n = 10;
    cin>>n;

    int arr[n];
    for (int i = 0; i < n; i++){
        cin >> arr[i];
    }
    int key;
    cin >> key;

    int result = ternarySearch(arr, 0, n - 1, key);

    if (result != -1)
    {
        cout << "Element found at index " << result << endl;
    }
    else
    {
        cout << "Element not found" << endl;
    }

    return 0;
}
