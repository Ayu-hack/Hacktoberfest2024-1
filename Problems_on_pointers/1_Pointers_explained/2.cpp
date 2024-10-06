#include<bits/stdc++.h>
using namespace std;

int main(){

    int a = 100;
    int *ptr = &a;

    a = a+1;
    // due to this line the value of the variable a gets incremented and pointer ptr still points to the 
    // same variable which now has a different value

    ptr = ptr+1;
    // This line states that the pointer now points to the next location of that particular datatype
    // let suppose the data-type of pointer is int and address is 104, then ptr points to address 108 as the 
    // integer variable takes 4 bytes of memory

    cout<<*ptr<<endl;

    /*
    
    NOTE - 
    
    Memory chart of different data-types
    
    char - 1 bytes
    bool - 4 bytes
    short - 2 bytes
    int - 4 bytes
    long - 8 bytes
    long long - 8 bytes
    float - 4 bytes 
    double - 8 bytes
    long double - 16 bytes
    */
}