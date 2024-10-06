#include<bits/stdc++.h>
using namespace std;

int main(){

    /*
    
    Ques - 
    
    Assume the memory address of variable a is 200 and a double variable is of size 8 bytes
    , what will be the output

    */ 
    
    double a = 10.54;
    double *d = &a;
    d = d+1;

    cout<<d<<endl;

    // d would now point to (200 + 8) bytes, which would point to memory address 208
}