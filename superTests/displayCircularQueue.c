void display()
{
int front_position = front;
int rear_position = rear;
if(front == -1)
{
printf("Queue underflow\n");
}
printf("The elements of the queue are:\n");
if( front_position <= rear_position )
while(front_position <= rear_position)
{
printf("%d\n",cqueue[front_position]);
front_position++;
}
else
{
while(front_position <= LIMIT-1)
{
printf("%d\n",cqueue[front_position]);
front_position++;
}
front_position = 0;
while(front_position <= rear_position)
{
printf("%d\n",cqueue[front_position]);
front_position++;
}
}
}
