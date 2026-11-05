from math import log2

data = ['243', '23', '123']
print(*map(lambda x: log2(float(x)), data))
