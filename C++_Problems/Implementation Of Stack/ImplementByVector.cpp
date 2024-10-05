// Implement stack using vector


#include<iostream>
#include<vector>
using namespace std;

class Stack{
    public:
        vector<int> arr;

        void pushIntoStack(int val){
           arr.push_back(val);
        }

        void popIntoStack(){
            if(arr.size() == 0){
                cout<<"Stack underflows occur"<<endl;
                return;
            } 
            arr.pop_back();
        }

        int getTopElement(){
            if(arr.size() == 0){
                cout<<"Stack underflows occur";
                return -1;
            } 
            return arr[arr.size() - 1];
        }

        int size(){
            return (arr.size() + 1);
        }

        void displayStack(){
            for(int i = 0;i < arr.size();i++){
                cout<<arr[i]<<" ";
            }
            cout<<endl;
        }
};

int main(){
    Stack st;
    // Underflow
    cout<<st.getTopElement()<<endl;

    // Push
    st.pushIntoStack(40);
    st.pushIntoStack(20);
    st.pushIntoStack(30);
    st.pushIntoStack(10);
    cout<<"Size of the stack after insertion : "<<st.size()<<endl;

    // Pop
    st.popIntoStack();
    cout<<"Size of the stack after deletion : "<<st.size()<<endl;

    // Top
    cout<<"Top element of the stack : "<<st.getTopElement()<<endl;

    // Size
    cout<<"Size of the stack : "<<st.size()<<endl;

    // display stack
    cout<<"Displaying stack : ";
    st.displayStack();

    // Over flow error
    st.pushIntoStack(50);
    st.pushIntoStack(60);
    st.pushIntoStack(70);
    cout<<"Displaying stack : ";
    st.displayStack();
}