void delet()
{
if (front == -1)
{
printf("Queue Underflow\n");
}
printf("Element deleted from queue is : %d\n",cqueue[front]);
if(front == rear) /* queue has only one element */
{
front = rear = -1;
}
else
{
if(front == LIMIT-1)
{
front = 0;
}
else
front++;
}
}
