#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """_summary_

    Args:
        my_list (list, optional): Input array of integers. Defaults to [].

    Returns:
        List: A list of the elements divisible and not divisible by 2
    """
    final_list = []
    final_list = [my_list[count] for count in range(len(my_list))
                  if my_list[count] % 2 == 0]
    return final_list
