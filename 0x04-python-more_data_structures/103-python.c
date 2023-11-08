#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - bytes information
 * @p: Object
 * Return: void
 */

void print_python_bytes(PyObject *p)
{
	char *s;
	long int size, i, l;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = ((PyVarObject *)(p))->ob_size;
	s = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", s);

	if (size >= 10)
		l = 10;
	else
		l = size + 1;

	printf("  first %ld bytes:", l);

	for (i = 0; i < l; i++)
		if (s[i] >= 0)
			printf(" %02x", s[i]);
		else
			printf(" %02x", 256 + s[i]);

	printf("\n");
}

/**
 * print_python_list - Prints list
 * @p: Object
 * Return: void
 */
void print_python_list(PyObject *p)
{
	long int s, i;
	PyListObject *list;
	PyObject *obj;

	s = ((PyVarObject *)(p))->ob_size;
	list = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", s);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < s; i++)
	{
		obj = ((PyListObject *)p)->ob_item[i];
		printf("Element %ld: %s\n", i, ((obj)->ob_type)->tp_name);
		if (PyBytes_Check(obj))
			print_python_bytes(obj);
	}
}
