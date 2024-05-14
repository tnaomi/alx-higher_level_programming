#include "lists.h"
/**
 * recCheckPalindrome - checks if singly linked list is palindrome
 * @left: pointer to head of singly linked list
 * @right: head of singly linked list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int recCheckPalindrome(listint_t **left, listint_t *right)
{
	int status;

	if (right == NULL)
		return (1);

	status = recCheckPalindrome(left, right->next);
	if (status == 0)
		return (0);

	status = (right->n == (*left)->n);

	*left = (*left)->next;

	return (status);
}
/**
 * is_palindrome - checks if singly linked list is palindrome
 * @head: pointer to head of singly linked list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	if (!head)
		return (0);
	return (recCheckPalindrome(head, *head));
}
