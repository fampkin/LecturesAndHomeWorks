with open('py_files/20/f.txt', 'r') as file:
    data = [int(x) for x in file.readlines()]
    print(min(data)+max(data))