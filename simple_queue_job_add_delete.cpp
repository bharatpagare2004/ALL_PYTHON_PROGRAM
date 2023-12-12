// this program for c++

#include<iostream>
using namespace std;
#define size 5

int queue[5],n = 5,front =-1,rear = -1;

// this function for insert the element
void insert()

{
    int val;
    if(rear == n-1)
    {
        cout<<"queue is overflow"<<endl;

    }
    else{
    if(front == -1)
    front =0;
    cout<<"insert the element:"<<endl;
    cin>>val;
    rear++;
    queue[rear]= val;

    
    
    }
}

//for deletion purpose
void delete1()
{
    if(front == -1|| front>rear){
    cout<<"queue is underflow";
    return;
    }
    else{
        cout<<"element deleted from queue is :"<<queue[front]<<endl;
        front++;
    }
    
    }
    void display1()
    {
        if(front == -1)
        cout<<"queue is empty"<<endl;
        else{
            cout<<"queue element are:"<<endl;
            for(int i = front ;i<=rear;i++)
            cout<<queue[i]<<" ";
             cout<<endl;


        }
    }

    int main()
    {
        int ch ;
        cout<<"1.insert the element"<<endl;
        cout<<"2.delete the element"<<endl;
        cout<<"3.display the element"<<endl;
        cout<<"4.exit"<<endl;
        do
        {
            cout<<"enter your choice";
            cin>>ch;
        

        switch(ch)
        {

            case 1:
            insert();
            break;
            case 2:
            delete1();
            case 3:
            display1();
            case 4:
            cout<<"exit";

        }
        }
        while(ch != 5);
        return 0;
        




        
        
    }



