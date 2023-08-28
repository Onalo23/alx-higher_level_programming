#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """ prints x elements of a list

    Arguments:
        my_list (list): The elements list from where to be printed
        x (int): the elements number of my_list to be printed

    Returns:
        the elements number printed
    """
    ret = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            ret += 1
        except IndexError:
            break
    print("")
    return (ret)
