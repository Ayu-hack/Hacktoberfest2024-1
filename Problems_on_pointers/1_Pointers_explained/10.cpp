#include<bits/stdc++.h>
using namespace std;

int main(){

    char ch[50] = "Statement";
    char *cptr = &ch[0];

    cout<<ch<<endl;//Statement
    cout<<&ch<<endl;//base address of the char array
    cout<<*(ch+3)<<endl;//t
    cout<<cptr<<endl;// Prints the whole character array
    cout<<&cptr<<endl;//address of cptr and not first element!
    cout<<*(cptr+3)<<endl;//char[3] = t
    cout<<cptr+2<<endl;// prints whole char array ahead of a inclusive a!
    cout<<*cptr<<endl;//S
    cout<<cptr+8<<endl;//t





}