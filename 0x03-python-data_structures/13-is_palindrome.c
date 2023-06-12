#include "lists.h"

/**
 * reverse - reverses the second half of the list
 *
 * @h_r: head of the second half
 * Return: no return
 */
void reverse(listint_t **h_r)
{
	listint_t *previous;
	listint_t *current;
	listint_t *mv;

	previous = NULL;
	current = *h_r;

	while (current != NULL)
	{
		mv = current->next;
		current->next = previous;
		previous = current;
		current = mv;
	}

	*h_r = previous;
}


/**
 * compare - compares each int of the list
 *
 * @h1: head of the first half
 * @h2: head of the second half
 * Return: 1 if are equals, 0 if not
 */
int compare(listint_t *h1, listint_t *h2)
{
	listint_t *tmp_1;
	listint_t *tmp_2;

	tmp_1 = h1;
	tmp_2 = h2;

	while (tmp_1 != NULL && tmp_2 != NULL)
	{
		if (tmp_1->n == tmp_2->n)
		{
			tmp_1 = tmp_1->next;
			tmp_2 = tmp_2->next;
		}
		else
		{
			return (0);
		}
	}

	if (tmp_1 == NULL && tmp_2 == NULL)
	{
		return (1);
	}

	return (0);
}

/**
 * is_palindrome - checks if a singly linked list
 * is a palindrome
 * @head: pointer to head of list
 * Return: 0 if it is not a palindrome,
 * 1 if it is a palndrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *slows, *go, *slows_prevs;
	listint_t *scn_half, *fix;
	int princ;

	slows = go = slows_prevs = *head;
	fix = NULL;
	princ = 1;

	if (*head != NULL && (*head)->next != NULL)
	{
		while (go != NULL && go->next != NULL)
		{
			go = go->next->next;
			slows_prevs = slows;
			slows = slows->next;
		}

		if (go != NULL)
		{
			fix = slows;
			slows = slows->next;
		}

		scn_half = slows;
		slows_prevs->next = NULL;
		reverse(&scn_half);
		princ = compare(*head, scn_half);

		if (fix != NULL)
		{
			slows_prevs->next = fix;
			fix->next = scn_half;
		}
		else
		{
			slows_prevs->next = scn_half;
		}
	}

	return (princ);
}
