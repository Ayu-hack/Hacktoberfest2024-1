#include<bits/stdc++.h>
using namespace std;

int main(){


    int arr[5] = {1, 2, 3, 4, 5};

    // int *ptr = arr;
    // This would store the base address of the integer array
    
    // int* ptr = &arr is wrong because the pointer is (pointer to an integer) whereas we want pointer to point to the array,
    // Therefore it shows error!

    // Syntax for a pointer to an integer array of size 5
    int (*ptr)[5] = &arr;
    cout<<(*ptr)[0]<<endl;

    char ch[10] = "Babbar";
    char* cptr = ch;

    // Difference between array of pointers and pointer to an array
    
    /*
    
    Pointer to an array-
    int (*ptr)[5];
    
    Array of pointers-
    int *arr[5]
    
    */

   // Array of pointers example is given below

   int *arr[5];

   int nums[5] = {1, 2, 3, 4, 5};
   





}