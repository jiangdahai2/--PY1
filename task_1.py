from pprint import pprint # TODO решить с помощью list comprehension и распечатать его
"""
"dec" - десятичное число
"bin" - двоичное число
"oct" - восьмеричное число
"hex" - шестнадцатеричное число
"""

list = [{'dec': num, 'bin': bin(num), 'oct': oct(num), 'hex': hex(num)} for num in range(16)]
pprint(list)