node* create_node(int x,int y){
struct node*temp;
temp=new(struct node);
if(temp==NULL){
cout<<"\nMemory not allocated";
return 0;
}
else{
temp->seatc=x;
temp->seatr=y;
temp->status="A";
temp->next=NULL;
temp->prev=NULL;
return temp;
}

}
void book(){
int x,y;
cout<<"\nEnter row and column";
cin>>x>>y;
struct node* temp;
temp=head[x-1];
for(int i=0 ; i<7 ; i++){
if(temp->seatc==y){
 if(temp->status=="A"){
  temp->status="B";
 }
 else{
  cout<<"\nSORRY !! Already booked!!";
 }
}
temp=temp->next;
}
display();
}

void cancel(){
int x,y;
cout<<"\nEnter row and column to cancel booking : ";
cin>>x>>y;
struct node* temp;
temp=head[x-1];
for(int i=0 ; i<7 ; i++){
if(temp->seatc==y){
 if(temp->status=="B"){
  temp->status="A";
 }
 else{
  cout<<"\nSORRY !! Already unbooked!!";
 }
}
temp=temp->next;
}
display();
}

void display(){
struct node* temp;
for(int j=0 ; j<10 ; j++){
temp=head[j];
for(int i=0 ; i<7 ; i++){
cout<<temp->seatr<<","<<temp->seatc;
cout<<""<<temp->status<<"\t";
temp=temp->next;
}
cout<<"\n";
}
}

};

int main(){
ticket t;
int ch;
t.display();
do{
 cout<<"\n1.Book Ticket \n2.Cancel Booking  \n3.EXIT";
 cin>>ch;
 switch(ch){
 case 1:t.book();break;
 case 2:t.cancel();break;
 }
}while(ch!=3);

return 0;
}
