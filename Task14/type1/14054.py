from itertools import count
from string import printable as pri

num = 2 * 2187 ** 567 + 729 ** 566 - 2 * 243 ** 565 + 81 ** 564 - 2 * 27 ** 563 - 6561
v7 = ''
while num:
    v7 += pri[num % 27]
    num //= 27
v7 = v7[::-1]
print(v7)
print(int(v7.count('q'))+int(v7.count('9'))+int(v7.count('i')))
