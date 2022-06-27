#include "lists.h"
/**
 * check_cycle - a function that cheks for tghe presence of a cycle
 * @list: the list to be checked
 * Return: 1 or 0
 */

int check_cycle(listint_t *list)
{
	int n;

	if (list == NULL)
		return (0);
	while (list->next)
	{
		n = list - list->next;
		if (n > 0)
			list = list->next;
		else
			return (1);
	}
	return (0);
}
