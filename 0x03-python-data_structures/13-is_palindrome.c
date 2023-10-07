#include "lists.h"

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: pointer to head of the linked list
 * Return: (1) if palindrome, (0) otherwise
 */

int is_palindrome(listint_t **head)
{
	listint_t *slow, *fast, *prev, *temp;

	if (*head == NULL)
		return (1);

	slow = *head;
	fast = *head;
	prev = NULL;
	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;

		temp = slow->next;
		slow->next = prev;
		prev = slow;
		slow = temp;
	}

	if (fast != NULL)
		slow = slow->next;

	while (prev != NULL && slow != NULL)
	{
		if (prev->n != slow->n)
			return (0);
		prev = prev->next;
		slow = slow->next;
	}

	return (1);
}

