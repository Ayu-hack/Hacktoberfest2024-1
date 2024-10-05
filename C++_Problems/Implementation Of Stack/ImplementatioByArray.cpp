// Implement stack using array


#include<iostream>
using namespace std;

class Stack{
    public:
        int arr[5];
        int idx;
        Stack(){
            idx = - 1;
        }

        void pushIntoStack(int val){
            if(idx == sizeof(arr) / sizeof(arr[0]) - 1){
                cout<<"Stack overflow occurs"<<endl;
                return;
            }
            idx++;
            arr[idx] = val;
        }

        void popIntoStack(){
            if(idx == -1){
                cout<<"Stack underflow occurs"<<endl;
                return;
            }
            idx--;
        }

        int getTopElement(){
            if(idx == -1){
                cout<<"Stack underflow occurs"<<endl;
                return -1;
            }
            return arr[idx];
        }

        int size(){
            return (idx + 1);
        }

        void displayStack(){
            for(int i = 0;i < idx;i++){
                cout<<arr[i]<<" ";
            }
            cout<<endl;
        }
};

int main(){
    Stack st;
    // Underflow
    cout<<st.getTopElement();

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