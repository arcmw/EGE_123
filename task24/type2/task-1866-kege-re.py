from re import finditer

with open(r"C:\Users\User\Downloads\task24\24_1866.txt") as f:
    data = f.read()

pattern = r'(a[^d]|d[^a])[^ad]*'



