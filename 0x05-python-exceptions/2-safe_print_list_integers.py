#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """ prints the first x elements of a list and only integers

    Arguments:
        my_list: (list) the elements list to be print from
        x: (int) the elements number of my_list to be printed

    Returns:
        the elements number printed
    """
    ret = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            ret += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (ret)
