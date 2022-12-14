void insert()
{
if((front == 0 && rear == LIMIT-1) || (front == rear+1))
{
printf("Queue Overflow\n");
}
if (front == -1) //If queue is empty
{
front = rear = 0;
}
else
{
printf("Enter the element to be inserted in queue: ");
scanf("%d", &item);
if(rear == LIMIT-1) // When rear is at the last position of the queue
{
rear = 0;
}
else
{
rear++;
}
}
cqueue[rear] = item ;
}
