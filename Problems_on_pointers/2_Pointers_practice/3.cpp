#include<bits/stdc++.h>
using namespace std;

int main(){

    int *ptr = 0;// pointer points to null
    // This is a good practice to declare a null pointer
    // a bad practice to declare a null pointer would be as shown below
    // int *ptr;
    int a = 10;
    *ptr = a;

    cout<<*ptr<<endl;

    // Output : This won't print anything as the pointer now points nowhere!
}