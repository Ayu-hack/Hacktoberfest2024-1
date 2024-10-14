#include <iostream>
#include <vector>
using namespace std;

int interpolationSearch(const vector<int>& list, int key) {
    int lo = 0, hi = list.size() - 1;

    // Handle the edge case of a single element list
    if (lo == hi) {
        if (list[lo] == key) {
            return lo;
        } else {
            return -1;
        }
    }

    while (lo <= hi && key >= list[lo] && key <= list[hi]) {
        // If the list has identical values
        if (list[hi] == list[lo]) {
            if (list[lo] == key) {
                return lo;
            } else {
                return -1;
            }
        }

        // Estimating the position using interpolation formula
        int pos = lo + ((key - list[lo]) * (hi - lo)) / (list[hi] - list[lo]);

        // Ensure pos is within the bounds of the list
        if (pos < lo || pos > hi) {
            return -1;
        }

        // Check if the estimated position holds the key
        if (list[pos] == key) {
            return pos;
        }

        // If the key is larger, search the right subarray
        if (list[pos] < key) {
            lo = pos + 1;
        }
        // If the key is smaller, search the left subarray
        else {
            hi = pos - 1;
        }
    }

    return -1;
}

int main() {
    cout << "Interpolation Search using C++" << endl;

    cout << "Please enter a list of sorted numbers (in ascending order) separated by spaces: ";
    vector<int> list1;
    int num;

    // Reading input numbers
    while (cin.peek() != '\n') {
        cin >> num;
        list1.push_back(num);
    }

    // Handle the edge case of an empty list
    if (list1.empty()) {
        cout << "The list is empty, no search can be performed." << endl;
        return 0;
    }

    int find;
    cout << "Enter the value you want to search for: ";
    cin >> find;

    int foundOn = interpolationSearch(list1, find);

    if (foundOn != -1) {
        cout << "Your given input " << find << " was found at position " << foundOn << "!" << endl;
    } else {
        cout << find << " is absent in the list!" << endl;
    }

    return 0;
}
