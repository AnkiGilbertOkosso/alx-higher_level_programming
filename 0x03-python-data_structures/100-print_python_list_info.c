#include <stdio.h>
#include <Python.h>


/**
 * print_python_list_info - prints python list info
 *
 * @p: PyObject
 * Return: no return
 */
void print_python_list_info(PyObject *p)
{
        long int new_size, n;
        PyListObject *list;
        PyObject *item;

        new_size = Py_SIZE(p);
        printf("[*] Size of the Python List = %ld\n", new_size);

        list = (PyListObject *)p;
        printf("[*] Allocated = %ld\n", list->allocated);

        for (n = 0; n < new_size; n++)
        {
                item = PyList_GetItem(p, n);
                printf("Element %ld: %s\n", n, Py_TYPE(item)->tp_name);
        }
}
