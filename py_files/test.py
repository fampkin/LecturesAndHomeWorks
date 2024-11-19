for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            f = not((x <= y) == (not (x and y) and z))
            print(x, y, z, f)