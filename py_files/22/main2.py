import re

with open('py_files/22/t.txt') as file:
    data = " ".join([x for x in file.readlines()])

dates = re.findall('([1-9]|1[0-9]|2[0-9]|3[0-1]|0[0-9])(.|-|\/)([1-9]|1[0-2]|0[0-9])(.|-|\/)(20[0-9][0-9])',data)

dates = [''.join(dates[i]) for i in range(len(dates))]

print(dates)