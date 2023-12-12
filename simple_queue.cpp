// this program for simple queue
#include<iostream>
using namespace std;
#define size 5

// inti
int queue[5],n= 5,front = -1,rear = -1;
// for insert the element
void insert()
{
    int val;
    if(rear == n-1){
    cout<<"queue is over flow"<<endl;
    }
    else{
        if(front == -1)
        front = 0;
        cout<<"insert the element:"<<endl;
        cin>>val;
        rear ++;
        queue[rear] = val;
      

    }

}
void delete1()
{

    if(front == -1||front>rear){
    
     cout<<"queue is underflow"<<endl;
     return ;}
    else{
        cout<<"element deleted is "<<queue[front]<<endl;
        front++;
    }

}

void display1()
{
    if(front == -1)
    cout<<"queue is empty"<<endl;
    
    else{
        cout<<"queue element is :"<<endl;
        for(int i = front;i<=rear ;i++)
        cout<<queue[i]<<" ";
         cout<<endl;
    }
}

int main()
{
    int ch;
    cout<<"1.inse"<<endl;
    cout<<"2.dis"<<endl;
    cout<<"3.del"<<endl;
    cout<<"exit"<<endl;
    do
    {
        cout<<"enter your choice:";
        cin>>ch;
        switch(ch)
        {
            case 1:
            insert();
            break;
            case 2:
            display1();
            break;
            case 3:
            delete1();
            break;
            case 4:
             cout<<"wrong choice";
        }
        
    } while (ch !=5);
    
}