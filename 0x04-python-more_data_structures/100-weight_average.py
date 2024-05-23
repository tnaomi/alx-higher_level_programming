#!/usr/bin/python3

def weight_average(my_list=[]):

    w_avg, mult = 0, 1
    multis, denom, ops = [], [], []
    if my_list is not None:
        for row in my_list:
            if len(row) == 2:
                i = 1
                for column in row:
                    mult *= column
                i += 1
                multis.append(mult)
                if i == len(row):
                    denom.append(column)
                mult = 1
        ops.extend((sum(multis), sum(denom)))
        w_avg = ops[0] / ops[1]
    return w_avg
