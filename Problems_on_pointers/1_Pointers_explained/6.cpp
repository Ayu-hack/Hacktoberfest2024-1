// Pointers with array!


#include<bits/stdc++.h>
using namespace std;

int main(){

    int arr[] = {10, 20, 30, 40, 50};

    int n = sizeof(arr) / sizeof(arr[0]);
    /*
    
    NOTE -
    
    In case of an array, 
    arr, &arr and &arr[0] all of these points to the BASE ADDRESS of the array!*/
    cout<<arr<<endl;
    cout<<&arr<<endl;
    cout<<&arr[0]<<endl;
    cout<<endl;

    for(int i = 0; i < n; i++){

        cout<<(&arr[i])<<endl;
    }

    cout<<endl;

    cout<<arr<<endl;
    // this would also print the base address of the array
    cout<<&arr<<endl;
    // This would store the base address of the array
    cout<<&arr<<endl; 
    // This would print the base address of the array
    cout<<*arr<<endl; 
    // This would give us the value of first element in the array - 10
    
    cout<<&arr[0]<<endl; 
    // This would give us the address of the first element in the array
    
    cout<<*arr+1<<endl; 
    // This would give us the value of the first element of array added 1 - 11
    cout<<*(arr)+1<<endl;

    cout<<*(arr+1)<<endl;
    // This would print the value one ahead of the pointer to the first element
    // arr POINTER!! points to the first element
    // if we add one to it (4 bytes as it is int pointer), points to the second element of the array as the array elements are contigious!
    // Thus prints 20
    // all of them downwards are similar!!
    cout<<*(arr+2)<<endl;
    cout<<*(arr+3)<<endl;

    /* 
    
    NOTES - 
    
    *(arr + 0) Points to the 0th element
    *(arr + 1) Points to the 1st element
    *(arr + 2) Points to the 2nd element
    *(arr + i) Points to the ith element in the array
    *(arr + i) is equivalent to i[arr]; // this is the most important thing you need to keep in mind!!

    
    */
}