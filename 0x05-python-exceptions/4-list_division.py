#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """ Function that divides two lists, element by element

    Args:
        my_list_1 : First list
        my_list_2 : Second list
        list_length : desired length of result list

    Returns:
        _list_ : a list of all the division results
    """
    div, divs = 0, []
    if my_list_1 is None or my_list_2 is None or list_length == 0:
        return div

    for indx in range(list_length):
        try:
            div = my_list_1[indx] / my_list_2[indx]

        except Exception as X:
            if isinstance(X, IndexError):
                print("out of range")
            elif isinstance(X, ZeroDivisionError):
                print("division by 0")
            elif isinstance(X, TypeError):
                print("wrong type")
            div = 0

        finally:
            divs.append(div)
    return divs
