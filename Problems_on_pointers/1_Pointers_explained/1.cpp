#include<bits/stdc++.h>
using namespace std;

int main(){

    int a = 5;

    // Printing the variable
    cout<<a<<endl;

    // Printing the address of the variable
    cout<<"Address of variable a : "<<&a<<endl;

    // Pointer to an integer variable
    int *ptr = &a;
    
    // another method to print the address of the variable
    cout<<"Address of variable : "<<ptr<<endl;

    /*
    
    NOTES -
    
    Address of operator - &
    // you might have also seen the address of operator
    while using scanf in C
    
    Value at address operator - *
    // this would help in dereferencing the operator and print the value stored at address
    
    */

   cout<<"Value at address : "<<*(ptr)<<endl;

   int size_of_integer_variable = sizeof(ptr);

   char ch = 'K';
   char *ptr2 = &ch;

   bool flag = false;
   bool *ptr3 = &flag;

   long lachi = 10;
   long *ptr4 = &lachi;
   
   int size_of_char_variable = sizeof(ptr2);
   int size_of_bool_variable = sizeof(ptr3);
   int size_of_long_variable = sizeof(ptr4);

   cout<<size_of_integer_variable<<endl;
   cout<<size_of_char_variable<<endl;
   cout<<size_of_bool_variable<<endl;
   cout<<size_of_long_variable<<endl;
   
   /*
   
   NOTE -
   
   In case of Pointers, size of all the pointers i.e. either it is a pointer to an
   integer variable, or a pointer to character variable or a pointer to bool variable
   or a pointer to long variable, the size will remain the same as it stores the address
   in each of the case and not the data itself!
   
   */
}