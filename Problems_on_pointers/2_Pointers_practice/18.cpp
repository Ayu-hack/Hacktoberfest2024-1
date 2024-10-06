#include<bits/stdc++.h>
using namespace std;

int main(){

    int numbers[5];
    int *p;
    p = numbers;//stored address of first element
    *p = 10;//first value of array assigned as 10
    p = &numbers[2];//stored address of third element
    *p = 20;//third element assigned value 20
    p--;// address comes to second value of array
    *p = 30;// second value is assigned as 30
    p = numbers+3;//address comes to fourth value
    *p = 40;// fourth value assigned as 40
    p = numbers;//base address again
    *(p+4) = 50;// base address + 4 ahead points to 5th place in array
    // fifth element is assigned value 50

    for(int n = 0; n < 5; n++){

        cout<<numbers[n]<<",";
    }
    // printing all the values in the array
    return 0;
}