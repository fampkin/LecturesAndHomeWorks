import regex

pattern = "^([1-9] |1[0-9]| 2[0-9]|3[0-1])(.|-)([1-9] |1[0-2])(.|-|)20[0-9][0-9]$"

date = input()
if regex.match(pattern, date):
    print('Yes')
else:
    print('No')
