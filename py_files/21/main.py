def find_all_matrixes(data):
    c = 0
    mms1 = dict()
    for i in range(len(data)):
        if data[i] == '':
            c += 1
        else:
            mms1[c] = mms1.get(c, []) + [data[i]]
    print(mms1)
    return mms1


with open('py_files/21/f1.txt', 'r') as file1, open('py_files/21/f2.txt', 'r') as file2:
    data1 = [x.strip() for x in file1.readlines()]
    data2 = [x.strip() for x in file2.readlines()]
    d1 = find_all_matrixes(data1)
    d2 = find_all_matrixes(data2)


for key, value in d2.items():
    last_n_d1 = list(d1.keys())[-1]
    d1[last_n_d1+1] = value
with open('py_files/21/f1.txt', 'w') as file:
    for value in d1.values():
        file.writelines([x+'\n' for x in value] + ['\n'])
