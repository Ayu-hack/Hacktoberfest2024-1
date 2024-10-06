#include<stdio.h>
#include<iostream>
#include<stdlib.h>
using namespace std;
class QUEUE
{
    private :
          int capacity ,front,rear,*ptr;

    public :
          QUEUE(int);
          void insert(int);
          void viewr_rear();
          void view_front();
          void delete_front();
          bool isempty();
          bool isfull();
          int count();      
};
QUEUE::QUEUE(int cap)
{
    capacity = cap;
    front = -1;
    rear =-1;
    ptr = new int[capacity];
}
bool QUEUE::isempty()
{
    return front==-1;
}
bool QUEUE::isfull()
{
    return (rear==capacity-1&&front==0 || rear+1==front );
}
void QUEUE::viewr_rear()
{
    cout<<ptr[rear];
}
void QUEUE::view_front()
{
    cout<<ptr[front];
}
int QUEUE::count()
{
    if (rear == -1 && front ==-1)
     return 0;
    else if (rear==front )
     return 1;
    else if (rear>front)
     return rear-front+1;
    else 
      return capacity - front+rear+1;
}
void QUEUE::insert(int data)
{
    if(isfull())
    {
        cout<<"OVERFLOW";
    }
    if (rear==-1 && front==-1)
    {
      rear=front=0;
      ptr[rear]=data;
    }
    else if(rear == capacity-1)
    {
      rear = 0;
      ptr[rear]=data;
    }
    else 
    {
      rear++;
      ptr[rear]=data;
    }
}
void QUEUE::delete_front()
{
    if (isempty())
        cout<<"UNDERFLOW";
    else if (front==rear)
       front=rear=-1;
    else if (front==capacity-1)
        front = 0;
    else 
       front++;   
}
int main()
{
    int cap,choice;
    cout<<"Enter capacity";
    cin>>cap;
    QUEUE q(cap);
    while(1)
    {
       cout<<"---MENU---\n";
       cout<<"1.INSERT\n";
       cout<<"2.COUNT\n";
       cout<<"3.VIEW REAR\n";
       cout<<"4.VIEW FRONT\n";
       cout<<"5.DELETE\n";
       cout<<"6.EXIT\n";
       cout<<"Enter a choice\n";
       cin>>choice;
       switch(choice)
       {
         case 1 :
               int data;
               cout<<"Enter data";
               cin>>data;
               q.insert(data);
               break;
         case 2 :
              int save;
              save = q.count();
              cout<<save;
              break;
         case 3 :
              q.viewr_rear();
              break;
         case 4 :
              q.view_front();
              break;
         case 5 :
              q.delete_front();
              break;
         case 6 :
              exit(0);
         default :
               cout<<"Wrong Choice \n";
       }
    }
}