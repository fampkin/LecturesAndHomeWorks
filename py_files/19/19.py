with open('py_files/19/test1.txt', 'r') as file:
    file_data_1 = file.readlines()
    
with open('py_files/19/test2.txt', 'r') as file:
    file_data_2 = file.readlines()
for i in range(len(file_data_2)):
    file_data_1[i] = file_data_1[i].strip() + file_data_2[i].strip() +'\n'

with open('py_files/19/test1.txt', 'w') as file:
    file.writelines(file_data_1)