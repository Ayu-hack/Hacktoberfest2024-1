#include<stdio.h>
#include<iostream>
using namespace std;
struct node 
{
   int pr;
   int item;
   node *next;
   node *prev;
};
class Pr
{
   private :
         node *start;

   public :
         Pr();
         void insert(int,int);
         void del();
         int getElement();
         int getNumber();
         bool isEmpty();
         ~Pr();
};
Pr::Pr()
{
    start = NULL;
}
void Pr::insert(int priority,int data)
{
    node *n;
    n = new node;
    n->item = data; 
    n->pr = priority;
    if (start == NULL)
    {
       n->pr = priority;
       n->next = NULL;
    }
    else
    {
        node *t;
        t = start;
        if (t->pr<n->pr)
        {
           
        }
        else 
        {
            t = t->next;
        }
    }
}