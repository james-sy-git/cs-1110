"""
User interface for module currency

When run as a script, this module prompts the user for two currencies and
an amount. It prints out the result of converting the first currency to
the second.

Author: James Sy (jcs547), Cella Schnabel (rms428)
Date: 22 September 2021
"""

import a1

src = input('Enter original currency: ')
dst = input('Enter desired currency: ')
amt = float(input('Enter original amount: '))

haha = a1.exchange(src, dst, amt)

print('You can exchange ' + str(amt) + ' ' + str(src) + ' for ' \
 + str(haha) + ' ' + str(dst) + '.')
