#include "lists.h"

/**
 *check_cycle - check if a linked list is circular or not
 *@list: the linked list
 *Return: 1 if there is a cycle 0 if not a cycle
 */
int check_cycle(listint_t *list)
{
	list *temp = head;

	while(temp != NULL)
	{
		if (temp->next == head)
		{
			return (1);
		}
		temp = temp->next;
	}
	return (0);
}
