// Variation in the character array

#include<bits/stdc++.h>
using namespace std;

int main(){

    char ch[50] = "love";
    
    char *cptr = ch;// stores the base address of char arrray
    // ch, &ch, &ch[0] all gives the base address of the character array
    
    cout<<cptr<<endl;
    // This donot print the value inside cptr which would be the address of the base element
    // In the character array, it prints whole character array!! i.e. love

    cout<<ch<<endl;//love
    cout<<&ch<<endl;//address pf the first element
    cout<<ch[0]<<endl;//l
    cout<<&cptr<<endl;//address of cptr
    cout<<*cptr<<endl;//value at base address of char array. OR value of first element  cptr[0]! or *(cptr+0)
    cout<<cptr<<endl;//love
}