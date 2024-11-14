for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            A = x <= ((y<=z) <= (y and z))
            B = (x or (y <= z)) and (x != y)
            print (x, y, z, A, B)