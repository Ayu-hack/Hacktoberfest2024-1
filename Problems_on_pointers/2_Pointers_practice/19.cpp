#include<bits/stdc++.h>
using namespace std;

int main(){

    char st[] = "ABCD";
    for(int i = 0; i != '\0'; i++){

        cout<<st[i]<<" "<<*(st)+i<<" "<<*(i+st)<<" "<<i[st];
        // all are equivalent and thus prints the same value.

    }

}
/*

OUTPUT : 

        A 65 A A
        B 66 B B
        C 67 C C
        D 68 D D
*/