from re import finditer

with open(r'C:\Users\User\Downloads\task24\24_1975.txt') as f:
    data = f.read()

pattern = r'[QRS]*P(([QRS])+P)+[QRS]*'

matches =  [match.group() for match in finditer(pattern, data)]

print(len(max(matches, key=len)))

