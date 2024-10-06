#include<bits/stdc++.h>
using namespace std;

int main(){

    char arr[20];
    int i;
    for(int i = 0; i < 10; i++){

        *(arr+i) = 65+i;

    }
    *(arr+i) = '\0';
    
    cout<<arr;
    return 0;

    // output : ABCDEFGHIJ
    // cause it is a character array

}