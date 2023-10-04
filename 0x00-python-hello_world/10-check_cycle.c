#include "lists.h"

int check_cycle(listint_t *list)
{
	listint_t *current = list;

	while (current != NULL)
	{
		listint_t *tmp_iter = list;
		if (current == current->next)
			return (1);
		while (tmp_iter != current)
		{
			if (current->next == tmp_iter)
				return (1);
			tmp_iter = tmp_iter->next;
		}
		current = current->next;
	}
	return (0);
}
