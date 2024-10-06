#include<bits/stdc++.h>
using namespace std;

int main(){

    int a = 7;
    int *c = &a;
    c = c+3;
    // Ques - Assume the memory address of a is 400 currently, what will be the output
    // Output : 
    /*
    400+(3*4)
    412
    cause of increment of 3 *integer size in the current memory address!
    */
}