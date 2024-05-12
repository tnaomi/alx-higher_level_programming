#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - insert a new node into a linked list
 * @head: pointer to head of list
 * @number: value of new node
 * Return: new node address or NULL if error
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = malloc(sizeof(listint_t)), *store = *head;
	listint_t *store2 = malloc(sizeof(listint_t));

	if (head == NULL || new_node == NULL)
		return (NULL);

	new_node->n = number;

	if (store == NULL || store->n >= number)
	{
		new_node->next = store;
		*head = new_node;
		return (new_node);
	}

	store2 = store->next;
	while (store && store2 && (store2->n < number))
	{
		store = store->next;
		store2 = store->next;
	}

	store->next = new_node, new_node->next = store2;

	return (new_node);

}
