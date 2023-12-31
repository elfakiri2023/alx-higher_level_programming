#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - if list contains a cycle.
 * @list: list
 * Return: If there is no cycle - 0.
 */
int check_cycle(listint_t *list)
{
	listint_t *s, *f;

	if (list == NULL || list->next == NULL)
		return (0);

	s = list->next;
	f = list->next->next;

	while (s && f && f->next)
	{
		if (s == f)
			return (1);

		s = s->next;
		f = f->next->next;
	}

	return (0);
}
