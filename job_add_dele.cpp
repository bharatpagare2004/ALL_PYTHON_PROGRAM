// this is for job add delete

#include<iostream>
using namespace std;
#define  size 5

int queue[5],n =5,rear =-1,front = -1;


// function for insert
void insert()
{
    int val;
    if(rear == n - 1)
    {
        cout<<"queue is overflow"<<endl;
    }
    else{
        if(front == -1)
        front = 0;
        cout<<"add the job"<<endl;
        cin>>val;
        rear ++;

        queue[rear] = val;
    }
}
//for delete
void delete1()
{
    if(front==-1||front>rear)
    {
    cout<<"queue is underflow"<<endl;
    return;}
    else
    { 
        cout<<"deleted job is"<<queue[front]<<endl;
        front++;

    } 
}
void display1()
{
    if(front == -1)
    cout<<"queue is empty"<<endl;
    else
    {
        cout<<"inserted job is "<<endl;
        for(int i = front ;i<=front;i++)
        cout<<queue[i]<<endl;
        cout<<endl;
    }
}

int main()
{
    int ch ;
    cout<<"1.insert the job"<<endl;
    cout<<"2.display the job"<<endl;
    cout<<"3.delete the job"<<endl;
    cout<<"4.exit"<<endl;
    do
   {
    cout<<"enter the choice";
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
   }
   }while(ch != 4);
   return 0;

}
   
   






  
