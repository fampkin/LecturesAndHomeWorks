from pprint import pprint
from random import randint

field_without_boats = [[0]*10 for _ in range(10)]
filed_with_boats = field_without_boats



def check_area_for_dot(x_dot:int ,y_dot:int) -> bool:

    left_pos = x_dot-1 if x_dot-1>=0 else 0
    right_pos = x_dot+1 if x_dot+1 <= 9 else 9
    top_pos = y_dot-1 if y_dot-1 >= 0 else 0
    bottom_pos = y_dot+1 if y_dot+1 <= 9 else 9

    for x in range(left_pos, right_pos):
        for y in range(top_pos, bottom_pos):
            if filed_with_boats[y][x] == 1:
                return False
    return True

def check_area_for_dots(poss_dots: list) -> bool:
    for x, y in poss_dots:
        if not check_area_for_dot(x, y):
            return False
    return True

def put_boat(size: int, count: int):
    """
    funtcion for set boat
    size - size of boat (1-4)
    count - count of boats
    """
    
    putted = 0

    while putted != count:
        x = randint(0, 9)
        y = randint(0, 9)
        dir = randint(1, 4) # direction for set boat 1-top, 2-right, 3-bottom, 4-left
        poss_for_boat = [[x, y]]
        match dir:
            case 1:
                if y-size+1>=0:
                    for i in range(y-size+1, y):
                        poss_for_boat.append([x, i])
                else:
                    continue
            case 3:
                if y+size-1<=9:
                    for i in range(y+1, y+size):
                        poss_for_boat.append([x, i])
                else:
                    continue
            case 2:
                if x+size-1<= 9:
                    for i in range(x+1, x+size):
                        poss_for_boat.append([i, y])
                else:
                    continue
            case 4:
                if x-size+1>= 0:
                    for i in range(x-size+1, x):
                        poss_for_boat.append([i, y])
                else:
                    continue

        if check_area_for_dots(poss_for_boat):
            for pos in poss_for_boat:
                print(pos)
                filed_with_boats[pos[1]][pos[0]] = 1
            putted += 1
     

put_boat(1, 4)
put_boat(2, 3)
put_boat(3, 2)
put_boat(4, 1)


pprint(filed_with_boats)