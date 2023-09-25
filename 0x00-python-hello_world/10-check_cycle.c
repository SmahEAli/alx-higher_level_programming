#include "lists.h"

/**
 * check_cycle - checker for cycle
 * @list: checker
 * Return: 1 if cycle or 0 if it no cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	if (!list)
		return (0);
	while (slow && fast && fast->nx)
	{
		slow = slow->nx;
		fast = fast->nx->nx;
		if (slow == fast)
			return (1);
	}
	return (0);
}
