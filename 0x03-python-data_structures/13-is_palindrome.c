#include "lists.h"

/**
 *is_palindrome - checking if a singly linked list is a palindrome
 *@head: the pointer to the starting node
 *Return: 0-not palindrome 1-if palindrome
 */
int is_palindrome(listint_t **head)
{
	int arraySize = 0, i, j, count = 0;

	while((*head) != NULL)
	{
		arraySize++;
		*head = (*head)->next;
	}

	int first[arraySize];
	int second[arraySize];

	if ((*head) == NULL)
	{
		return (1);
	}

	while ((*head) != NULL)
	{
		first[count] = (*head)->n;
		*head = (*head)->next;
		count++;
	}

	for (i = 0; i < arraySize; i++)
	{
		second[0] = first[(arraySize - 1) - i];
	}

	for (j = 0; j < arraySize; j++)
	{
		if (second[j] != first[j])
		{
			return (0);
		}
	}

	return (1);
}


/**
 *countNodes - counts the number of nodes in a singly linked list
 *Return: the count
 *
 *int countNodes(listint_t **head)
 *{
 *	int count = 0;
 *
 *	while((*head) != NULL)
 *	{
 *		count++;
 *		*head = (*head)->next;
 *	}
 *
 *	return (count);
 *}
 */
