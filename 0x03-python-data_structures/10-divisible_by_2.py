#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """_summary_

    Args:
        my_list (list, optional): Input array of integers. Defaults to [].

    Returns:
        List: A list of the elements divisible by 2 as a list of bools
    """
    final_list = [True if num % 2 == 0 else False for num in my_list]
    return final_list
