#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: points to the list
 * Return: 0 if there is no cycle else 1
 */
int check_cycle(listint_t *list)
{
	listint_t *point1;
	listint_t *point;

	point1 = list;
	point = list;
	while (list && point1 && point1->next)
	{
		list = list->next;
		point1 = point1->next->next;

		if (list == point1)
		{
			list = point;
			point = point1;
			while (1)
			{
				point1 = point;
				while (point1->next != list && point1->next != point)
				{
					point1 = point1->next;
				}
				if (point1->next == list)
					break;

				list = list->next;
			}
			return (1);
		}
	}
	return (0);
}
