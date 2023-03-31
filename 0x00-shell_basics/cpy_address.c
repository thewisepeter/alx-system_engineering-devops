#include "main.h"

/**
 * cpy_address - handles p
 * @args: argument list
 * @buff: buffer
 * @buff_loc: buffer position pointer
 * Return: number of chars printed
 */
int cpy_address(va_list args, char *buff, unsigned long int *buff_loc)
{
	int count, rem, i, len = 0;
	intptr_t ptr_1, ptr = va_arg(args, intptr_t);
	char *str;
	char hex[16] = "0123456789abcdef";

	buff[*buff_loc] = '0';
	*buff_loc = *buff_loc + 1;
	buff_check(buff, buff_loc);
	buff[*buff_loc] = 'x';
	*buff_loc = *buff_loc + 1;
	buff_check(buff, buff_loc);
	if (ptr == 0)
	{
		buff[*buff_loc] = '0';
		*buff_loc = *buff_loc + 1;
		buff_check(buff, buff_loc);
		return (1);
	}
	ptr_1 = ptr;
	for ( ; ptr_1 != 0; ptr_1 /= 16)
		len++;
	str = malloc(sizeof(char) * (len + 1));
	if (!str)
		return (-1);
	count = len;
	for (i = len - 1; i >= 0; i--)
	{
		rem = ptr % 16;
		ptr = ptr / 16;
		str[i] = hex[rem];
	}
	for (i = 0; i < len; i++)
	{
		buff[*buff_loc] = str[i];
		*buff_loc = *buff_loc + 1;
		buff_check(buff, buff_loc);
	}
	free(str);
	return (count + 2);
}
