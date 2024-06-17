#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - check if the singly-linked list has a cycle
 * @list: Singly-linked list
 * Return: 0 if no cycle, 1 if cycle.
 */
int check_cycle(listint_t *list)
{
	listint_t *store = malloc(sizeof(list));

	if (!store)
		return (0);

	while (list)
	{
		store = list;
		list = list->next;
		if (store < list)
			return (1);
	}

	return (0);
}
