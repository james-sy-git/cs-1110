"""
Test script for module a1

When run as a script, this module invokes several procedures that
test the various functions in the module a1.

Author: James Sy (jcs547) AND Cella Schnabel (rms428)
Date:   25 September 2021
"""

import introcs
import a1


def testA():
    """
    Test procedure for function before_space, after_space
    """
    print ('Testing before_space')

    # Normal
    introcs.assert_equals('7.8', a1.before_space('7.8 USD'))

    # Lots of space between
    result = a1.before_space('7.8                USD')
    introcs.assert_equals('7.8', result)

    # Space at beginning
    introcs.assert_equals('', a1.before_space(' 8USD'))

    # Multiple spaces in string
    introcs.assert_equals('7.', a1.before_space('7. 8 US D'))

    # Space at end
    introcs.assert_equals('USD', a1.before_space('USD '))

    # Lots of space at beginning
    introcs.assert_equals('', a1.before_space('     8USD'))

    print ('Testing after_space')

    # Normal
    introcs.assert_equals('USD', a1.after_space('7.8 USD'))

    # Nothing after space
    introcs.assert_equals('', a1.after_space('7.8 '))

    # Only space
    introcs.assert_equals('       ', a1.after_space('        '))

    # Multiple space in one string
    introcs.assert_equals('o p l ', a1.after_space('7 o p l '))


def testB():
    """
    Test procedure for function first_inside_quotes,
    get_new, get_old, has_error
    """

    print ('Testing first_inside_quotes')

    # Normal
    introcs.assert_equals('B C', a1.first_inside_quotes('A "B C" D'))

    # Nothing in quotes
    introcs.assert_equals('', a1.first_inside_quotes('A "" D'))

    # Two quotes
    introcs.assert_equals('B', a1.first_inside_quotes('A "B" "C" D'))

    #only quotes with something inside
    introcs.assert_equals('B', a1.first_inside_quotes('"B"'))

    print ('Testing get_new')

    # Normal
    introcs.assert_equals('50.212 Philippine Pesos',a1.get_new(\
    '{ "err":"", "old":"1 United States Dollar",\
     "new":"50.212 Philippine Pesos", "valid":true }'))

     # Nothing in new
    introcs.assert_equals('',a1.get_new('{ "err":"Currency amount is' + \
    ' invalid.", "old":"", "new":"", "valid":false }'))

    print ('Testing get_old')

    # Normal
    introcs.assert_equals('1 United States Dollar',a1.get_old('{ "err":\
    "", "old":"1 United States Dollar", "new":"50.212 Philippine\
     Pesos", "valid":true }'))

     # Nothing in old
    y= '{ "err":"Currency amount is invalid.",'+\
    ' "old":"", "new":"", "valid":false }'
    introcs.assert_equals('',a1.get_old(y))

    print ('Testing has_error')

    # Currency amount is invalid
    introcs.assert_equals(True, a1.has_error('{ "err":"Currency\
     amount is invalid.", "old":"", "new":"", "valid":false }'))

    # Source currency in invalid
    x= '{ "err":"Source currency code\
     is invalid.", "old":"", "new":"", "valid":false }'
    introcs.assert_equals(True, a1.has_error(x))

    # Exchange currency is invalid
    z= '{ "err":"Exchange currency code\
     is invalid.", "old":"", "new":"", "valid":false }'
    introcs.assert_equals(True, a1.has_error(z))

     # No error
    k= '{ "err":"", "old":"1 United States Dollar\
    ", "new":"50.212 Philippine Pesos", "valid":true }'
    introcs.assert_equals(False, a1.has_error(k))


def testC():
    """
    Test procedure for function query_website
    """

    print ('Testing query_website')

    # Normal
    introcs.assert_equals('{ "err":"", "old":"1 United States Dollar",' +
    ' "new":"50.212 Philippine Pesos", "valid":true }',
    a1.query_website('USD', 'PHP', 1.0))

    # Invalid Source Currency
    introcs.assert_equals('{ "err":"Source currency code is invalid.",'+
    ' "old":"", "new":"", "valid":false }',
    a1.query_website('idk','PHP', 1.0))

    # Invalid Exchange Currency
    introcs.assert_equals('{ "err":"Exchange currency code is invalid."'+
    ', "old":"", "new":"", "valid":false }',
    a1.query_website('USD','ttyl',1.0))

    # negative dollars!?
    introcs.assert_equals('{ "err":"", "old":"-2 United States'+\
     ' Dollars", "new":"-100.424 Philippine Pesos", "valid":true }'\
    , a1.query_website('USD', 'PHP', -2.0))


def testD():
    """
#    Test procedure for funtion is_currency, exchange
#    """
    print ('Testing is_currency')

    # All caps, not real currency
    introcs.assert_equals(False,a1.is_currency ('CMS'))

    # All caps, real currency
    introcs.assert_equals(True,a1.is_currency ('USD'))

    # Lowercase, real currency
    introcs.assert_equals(False,a1.is_currency ('usd'))

    # Not enough letters
    introcs.assert_equals(False,a1.is_currency ('ud'))

    # No letters
    introcs.assert_equals(False,a1.is_currency (''))


    print ('Testing exchange')

    # Normal
    introcs.assert_floats_equal(251.06,a1.exchange('USD', 'PHP', 5.0))

    # Negative amount
    introcs.assert_floats_equal(-251.06,a1.exchange('USD', 'PHP', -5.0))

testA()
testB()
testC()
testD()
print('Module a1 passed all tests.')
