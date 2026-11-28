from re import finditer

with open(r'C:\Users\User\PycharmProjects\EGE_123\files\task24\24_17685.txt') as file:
    data = file.readline()

num = r'([1-9]\d*|0)'
pattern = rf'({num}[+*])+{num}'

matches = [match.group() for match in finditer(pattern, data)]

ans = 0
for line in matches:
    len_line = len(line)
    if eval(line) == 0:
        ans = max(ans, len(line))
    elif len_line > ans:
        for l in range(len_line):
            if line[l] in '+*' or line[l] == '0' and line[l + 1] in '0123456789':
                continue
            for r in range(len_line - 1, l, -1):
                if line[r] in '+*':
                    continue
                if eval(line[l:r + 1]) == 0:
                    ans = max(ans, r - l + 1)
                    break
            if len_line <= ans:
                len_line = ans
print(ans)


###################################################################################


from re import finditer

with open(r'C:\Users\User\PycharmProjects\EGE_123\files\task24\24_17685.txt') as file:
    data = file.readline()



num = r'([1-9]\d*|0)'
zero = rf'({num}\*)*0(\*{num})*'
pattern = rf'({zero}\+)+{zero}'

matches = [match.group() for match in finditer(pattern, data)]

print(len(max(matches, key=len)))