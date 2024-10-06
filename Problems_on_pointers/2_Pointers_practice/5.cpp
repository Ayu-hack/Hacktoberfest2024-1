#include<bits/stdc++.h>
using namespace std;

int main(){

    char ch = 'a';
    char *ptr = &ch;
    ch++;

    cout<<*ptr<<endl;
    // NOTE - ascii value of a is 97 , would increment by 1, giving b in output
    // output : b

}