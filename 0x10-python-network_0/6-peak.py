#!/usr/bin/python3
""" finds a peak in a list of unsorted integers """


def find_peak(list_of_integers):
    """ find peak """
    max_ele = None
    for element in list_of_integers:
        if max_ele is None or max_ele < element:
            max_ele = element
    return max_ele
    