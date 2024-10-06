#include<bits/stdc++.h>
using namespace std;

int main(){

    float f = 10.5;
    float p = 2.5;

    float* ptr = &f;//address of f
    (*ptr)++;//11.5
    *ptr = p;//ptr value becomes 2.5

    cout<<*ptr<<" "<<f<<" "<<p;

    // output : 
    // 2.5 2.5 2.5
}