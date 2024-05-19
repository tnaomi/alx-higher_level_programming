#!/usr/bin/python3

def roman_to_int(roman_string):
    """ ### Returns a copy of __my_list__ with the multiple of number

    ### Args:
        roman_string (_str_): _Roman numeral string_.

    ### Returns:
        _int_: _Roman numeral to integer_
    """
    actual_no = 0

    def dict_sum(length, start=0, dct={}, romn=""):
        """Find the sum of corresponding integers of roman numerals

        Args:
            length (_int_): _Length of the roman numeral_
            start (_int_): _starting index_
            dct (_dict_): _A dictionary of roman numerals
            and corresponding values_
            romn (_str_): _Input roman numeral to be converted_

        Returns:
            _int_: _integer equivalent of a roman numeral_
        """
        summ = 0
        for i in range(start, length):
            current = dct[romn[i]]
            summ += current
        return summ

    if roman_string is not None:
        length = len(roman_string)
        roman = {"I": 1,
                 "V": 5,
                 "X": 10,
                 "L": 50,
                 "C": 100,
                 "D": 500,
                 "M": 1000}
        if length < 2:
            actual_no = roman.get(roman_string)
        else:
            op1, op2 = roman[roman_string[0]], roman[roman_string[1]]
            if op1 >= op2:
                actual_no = dict_sum(length, 0, roman, roman_string)
            else:
                store = op2 - op1
                if length == 2:
                    actual_no = store
                else:
                    actual_no = dict_sum(length, 2, roman, roman_string)
    return actual_no
