// Implement stack using Linked List


#include<iostream>
#include<vector>
using namespace std;

class Node{
    public:
        int val;
        Node* next;
        Node(int val){
            this->val = val;
            this->next = NULL;
        } 
};

class Stack{
    public:
        Node* head;
        int size;
        Stack(){
            head = NULL;
            size = 0;
        }

        void pushIntoStack(int val){
            Node* temp = new Node(val);
            temp->next = head;
            head = temp;
            size++;
        }

        void popIntoStack(){
            if(head == NULL){
                cout<<"Stack is in under flow";
                return;
            } 
            head = head->next;
            size--;
        }

        int getTopElement(){
            if(head == NULL){
                cout<<"Stack is in under flow";
                return -1;
            }
            return head->val;
        }

        int sizeOfStack(){
            return size;
        }

        void display(Node* head){
            Node* temp = head;
            if(temp == NULL) return;
            display(temp->next);
            cout<<temp->val<<" ";
        }
        void displayStack(){
            display(head);
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
    cout<<"Size of the stack after insertion : "<<st.sizeOfStack()<<endl;

    // Pop
    st.popIntoStack();
    cout<<"Size of the stack after deletion : "<<st.sizeOfStack()<<endl;

    // Top
    cout<<"Top element of the stack : "<<st.getTopElement()<<endl;

    // Size
    cout<<"Size of the stack : "<<st.sizeOfStack()<<endl;

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