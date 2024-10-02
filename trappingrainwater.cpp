// #include<bits/stdc++.h>
#include <iostream>
//for using the cout and cin in c++
#include <vector>
// Instead of including bits/stdc++.h, you can include the specific header files that you need for your program. For example, if you're using vectors, you can include vector instead
using namespace std;

int trap(vector<int>& height) {
    int n = height.size();
    int left = 0, right = n - 1;
    int res = 0;
    int maxLeft = 0, maxRight = 0;
    while (left <= right) {
        if (height[left] <= height[right]) {
            if (height[left] >= maxLeft) {
                maxLeft = height[left];
            } else {
                res += maxLeft - height[left];
            }
            left++;
        } else {
            if (height[right] >= maxRight) {
                maxRight = height[right];
            } else {
                res += maxRight - height[right];
            }
            right--;
        }
    }
    return res;
}

int main() {
    // vector<int> arr;
    int n;
    cout << "Enter the number of elements: ";
    cin >> n;
    if(n <= 0 )
    {
        cout << "Invalid Input";
        return 1;
    }

    vector<int> arr;
    cout << "Enter the height of each bar: ";
    for (int i = 0; i < n; i++) {
        int height;
        cin >> height;
        arr.push_back(height); 
    }
    
    int waterIn = trap(arr);
    cout << "The water that can be trapped is " << waterIn << endl;
    // cout << "The water that can be trapped is " << trap(arr) << endl;

    return 0;
}


/*


Time Complexity: O(N) because we are using 2 pointer approach.

Space Complexity: O(1) because we are not using anything extra.

*/
