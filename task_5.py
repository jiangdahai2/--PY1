from random import sample
import string
"""
Буквы верхнего регистра: A - Z →string.ascii_uppercase
Буквы нижнего регистра: a - z →string.ascii_lowercase
Цифры: 0 - 9 → string.digits
"""
def get_random_password(n=8) -> str:
    chars = sample(string.digits + string.ascii_lowercase + string.ascii_uppercase, n)


    return "".join(chars)


print(get_random_password())
