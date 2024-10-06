#include<bits/stdc++.h>
using namespace std;

void solve(int *arr, int size){

    *arr = *arr+1;
    // This would increment the first element of the array by 1
}

int main(){

    int arr[] = {10, 20, 30};


    solve(arr, 3);
    // this would increment the size of the first element by 1
    

    for(int i = 0; i < 3; i++){

        cout<<arr[i]<<" ";
    }


}