#include<bits/stdc++.h>
using namespace std;

int main(){

    float arr[5] = {12.5, 10.0, 13.5, 90.5, 0.5};
    float *ptr1 = &arr[0];// address of 12.5
    float *ptr2 = ptr1 + 3;// address of 90.5

    cout<<*ptr2<<" ";//90.5
    cout<<ptr2-ptr1;//(4*4 - 4*1) = 12 / 4 = 3
    return 0;

    // output : 90.5 3
}