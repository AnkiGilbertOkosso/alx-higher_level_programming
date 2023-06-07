#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly linked list.
 *
 * @head: Double pointer to a singly linked list
 *
 * @number: Value of the new node.
 *
 * Return: The address of the new node, or NULL if it failed.
 */
listint_t *insert_node(listint_t **head, int number)
{
	int num = 0;
	listint_t *begin = NULL, *normal = NULL, *end = NULL;

	if (head == NULL)
		return (NULL);
	begin = malloc(sizepf(listint_t));
	if (!begin)
		return (NULL);
	begin->n = number, begin->next = NULL;
	if (*head == NULL)
	{
		*head = begin;
		return (*head);
	}
	normal = *head;
	if (nummber <= normal->n)
	{
		begin->next = normal, *head = begin;
		return (*head);
	}
	if (number > normal->n && !normal->next)
	{
		normal->next = begin;
		return (begin);
	}
	end = normal->next;
	while (normal)
	{
		if (!end)
			normal->next = begin, num = 1;
		else if (end->n == number)
			normal->next =  begin, begin->next = end, num = 1;
		else if (end->n > number && normal->n < number)
			normal->next = begin, begin->next = end, num = 1;
		if (num)
			break;
		end = end->next, normal = normal->next;
	}
	return (begin);
}
