#include "lists.h"

/**
 *check_cycle - check if a linked list is circular or not
 *@list: the linked list
 *Return: 1 if there is a cycle 0 if not a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	slow = head;
	fast = head;

	if (head == NULL)
		return (0);

	while(temp->next != NULL && fast->next-next != NULL)
	{
		slow = slow->next;
		fast = fast->next-next;

		if (slow == fast)
			return (1);
	}
	return (0);
}
