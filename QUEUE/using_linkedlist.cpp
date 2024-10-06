#include<stdio.h>
#include<iostream>
#include<stdlib.h>
using namespace std;
struct node
{
    int item;
    node *next;
};
class QUEUE
{
    private :
          node *front ;//start
          node *rear ;

    public :
          QUEUE();
          void insert(int);
          void view_rear();
          void view_front();
          void delete_front();
          void display();
          void count();      
};
QUEUE::QUEUE()
{
    front = rear = NULL;
}
void QUEUE::insert(int data)
{
    node*n;
    n = new node;
    n->item = data;
    if (rear==NULL && front==NULL)
    {
        n->next = NULL;
        front=rear=n;
    }
    else 
    {
        n->next=front->next;
        front = n;
    }
}
void QUEUE::view_front()
{
    if (front==NULL)
      cout<<"List is Empty";
    else 
      cout<<front->item;
}
void QUEUE::view_rear()
{
    if (rear==NULL)
      cout<<"List is Empty";
    else 
      cout<<rear->item;
}
void QUEUE::delete_front()
{
    node *r;
    if(front==NULL)
        cout<<"LIST IS EMPTY";
    else if (front==rear)
      {
         r=front;
         delete []r;
         front=rear=NULL;
      }
    else 
      {
        r = front;
        front = r->next;
        delete []r;
      }
}
void QUEUE::count()
{
    int count = 0;
    node *t;
    t=front;
    while(t->next!=NULL)
       {
         count++;
         t=t->next;
       }
    cout<<count<<endl;
}
void QUEUE::display()
{
    node *t;
    t=front;
    while (t->next!=NULL)
    {
      cout<<t->item<<"  ";
      t=t->next;
    }
}
int main()
{
    QUEUE q;
    int choice;
    while(1)
    {
       cout<<"---MENU---\n";
       cout<<"1.INSERT\n";
       cout<<"2.COUNT\n";
       cout<<"3.VIEW REAR\n";
       cout<<"4.VIEW FRONT\n";
       cout<<"5.DELETE\n";
       cout<<"6.Display\n";
       cout<<"7.EXIT\n";
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
              q.count();
              break;
         case 3 :
              q.view_rear();
              break;
         case 4 :
              q.view_front();
              break;
         case 5 :
              q.delete_front();
              break;
         case 6 :
              q.display();
              break;
         case 7 :
              exit(0);
         default :
               cout<<"Wrong Choice \n";
       }
    }
}