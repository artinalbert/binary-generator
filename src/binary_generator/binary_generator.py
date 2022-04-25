from number_lib.conversions import binary_to_octal
from random import randint
import random


def binary_generator(n):
    p = ''
    for i in range(n):
        temp = str(random.randint(0, 1))

        # Concatenation the random 0, 1
        # to the final result
        p += temp

    binary_to_octal(p)

    return p


if __name__ == '__main__':
    ex = 7
    example = binary_generator(ex)
    print(f'Here is the random number: {example}')
