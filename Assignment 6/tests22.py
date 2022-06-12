"""
A unit test for Lab 22

Authors: Lillian Lee (LJL2) and Walker White (wmw2)
Date:    November 2, 2021
"""

import introcs
import funcs


def test_duplicate_copy():
    """
    Tests the function duplicate_copy
    """
    print('Testing duplicate_copy')
    introcs.assert_equals([5,5], funcs.duplicate_copy([5],5))
    introcs.assert_equals([], funcs.duplicate_copy([], 1))
    mylist = [5, 3, 3455, 74, 74, 74, 3]
    introcs.assert_equals([5, 3, 3, 3455, 74, 74, 74, 3, 3], funcs.duplicate_copy(mylist,3))
    introcs.assert_equals([5, 3, 3455, 74, 74, 74, 74, 74, 74, 3], funcs.duplicate_copy(mylist, 74))
    print('  duplicate_copy looks okay')


def test_duplicate():
    """
    Tests the function duplicate
    """
    print('Testing duplicate')
    mylist = [5]
    funcs.duplicate(mylist,5)
    introcs.assert_equals([5,5], mylist)

    mylist = []
    funcs.duplicate(mylist,1)
    introcs.assert_equals([], mylist)

    mylist = [5, 3, 3455, 74, 74, 74, 3]
    funcs.duplicate(mylist, 3)
    introcs.assert_equals([5, 3, 3, 3455, 74, 74, 74, 3, 3], mylist)

    funcs.duplicate(mylist, 74)
    introcs.assert_equals([5, 3, 3, 3455, 74, 74, 74, 74, 74, 74, 3, 3], mylist)
    print('  duplicate looks okay')


def test_exp():
    """
    Tests the function exp
    """
    print('Testing exp')
    introcs.assert_equals(2.71828,      round(funcs.exp(1),5))
    introcs.assert_equals(2.71828182846,round(funcs.exp(1,1e-12),11))
    introcs.assert_equals(0.13534,      round(funcs.exp(-2),5))
    introcs.assert_equals(0.13533528324,round(funcs.exp(-2,1e-12),11))
    introcs.assert_equals(2981.0,       round(funcs.exp(8,1e-1),0))
    introcs.assert_equals(2980.95799,   round(funcs.exp(8),5))
    introcs.assert_equals(2980.95798704173,round(funcs.exp(8,1e-12),11))
    print('  exp looks okay')


# Script Code
if __name__ == '__main__':
    test_duplicate_copy()
    test_duplicate()
    test_exp()

    print('The module funcs passed all tests')
