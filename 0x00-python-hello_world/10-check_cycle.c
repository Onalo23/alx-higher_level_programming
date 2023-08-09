#include "lists.h"

/**
 * check_cycle - checks if a linked list contains a cycle
 * @list: linkd list to be checked
 *
 * Return: if the list has a cycle 1, otherwise 0
 */
int check_cycle(listint_t *list)

{
	listint_t *slow = list;
	listint_t *fast = list;

	if (!list)
		return (0);

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
