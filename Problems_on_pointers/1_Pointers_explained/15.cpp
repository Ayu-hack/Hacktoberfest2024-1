// Pointer to pointers

#include<bits/stdc++.h>
using namespace std;

int main(){

    int a = 5;
    int *ptr = &a;

    int **ptr2 = &ptr;

    int *** ptr3 = &ptr2;

    int ****ptr4 = &ptr3;

    /*
    
    NOTE -
    
    ptr points to the address of a!
    ptr2 points to the address of ptr actully and not a!
    ptr3 points to the address of ptr2 and ptr4 points to the address of ptr3!

    */

    cout<<ptr<<endl;
    cout<<ptr2<<endl;
    cout<<ptr3<<endl;
    cout<<ptr4<<endl;

    cout<<endl;

    // We can ge the address of a from all of the above pointers

    cout<<ptr<<endl;
    cout<<ptr2<<endl;
    cout<<ptr3<<endl;
    cout<<ptr4<<endl;
}