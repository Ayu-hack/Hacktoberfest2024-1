#include<stdio.h>
#include<iostream>
using namespace std;
struct node 
{
   node *prev;
   int item;
   node *next;
};
class deque
{
     private : 
            node *rear , *front;
     
     public :
            deque();
            void insert_front(int);
            void insert_rear(int);
            void delete_front();
            void delete_rear();
            int  get_front();
            int  get_rear();
            bool isEmpty();
            ~deque();
};
deque::deque()
{
    rear = front = NULL;
}
void deque::insert_front(int data)
{
   node *n;
   n = new node ;
   n->prev = NULL;
   n->item = data;
   n->next = front;
   front = n;
}
void deque::insert_rear(int data)
{
    node *n ;
    n = new node;
    n->next = NULL;
    n->item = data;
    n->prev = rear;
    rear = n;
}
void deque::delete_front()
{
    if(front==NULL)
      cout<<"List Empty";
    node *r;
    r = front;
    front = r->next;
    front->prev = NULL;
    delete []r;
}
void deque::delete_rear()
{
     if(rear==NULL)
      cout<<"List Empty";
    node *r;
    r = rear;
    r->prev = rear;
    rear->next = NULL;
    delete []r;
}
int deque::get_front()
{
    if(front==NULL)
      cout<<"List Empty";
    return front->item;
}
int deque::get_rear()
{
    if(rear==NULL)
      cout<<"List Empty";
    return rear->item;
}
bool deque::isEmpty()
{
    return (rear==NULL && front==NULL);
}
deque::~deque()
{
    while(front)
       delete_front();
}