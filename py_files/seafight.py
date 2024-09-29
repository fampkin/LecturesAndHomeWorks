from pprint import pprint
from random import randint

field_without_ships = [['0']*10 for _ in range(10)]
filed_with_ships = field_without_ships
field_with_hide_ships = [['.']*10 for _ in range(10)]

ships_cords = []
ships_dead_cords = []

def check_area_for_dot(x_dot:int ,y_dot:int) -> bool:
    """
    Function for check one dot on area (dot and around dot)
    """
    left_pos = x_dot-1 if x_dot-1>=0 else 0
    right_pos = x_dot+1 if x_dot+1 <= 9 else 9
    top_pos = y_dot-1 if y_dot-1 >= 0 else 0
    bottom_pos = y_dot+1 if y_dot+1 <= 9 else 9

    for x in range(left_pos, right_pos+1):
        for y in range(top_pos, bottom_pos+1):
            if filed_with_ships[y][x] == '1':
                return False
    return True

def check_area_for_dots(poss_dots: list) -> bool:
    """
    Function for check all dots which will be "ship"
    """
    for x, y in poss_dots:
        if not check_area_for_dot(x, y):
            return False
    return True

def put_ship(size: int, count: int):
    """
    Function for set ship
    size - size of ship (1-4)
    count - count of ships
    """
    
    putted = 0

    while putted != count:
        x = randint(0, 9) # pos x for top/bottom/left/right start ship
        y = randint(0, 9) # pos x for top/bottom/left/right start ship
        dir = randint(1, 4) # direction for set ship 1-top, 2-right, 3-bottom, 4-left
        poss_for_ship = [[x, y]]
        match dir:
            case 1:
                if y-size+1>=0:
                    for i in range(y-size+1, y):
                        poss_for_ship.append([x, i])
                else:
                    continue
            case 3:
                if y+size-1<=9:
                    for i in range(y+1, y+size):
                        poss_for_ship.append([x, i])
                else:
                    continue
            case 2:
                if x+size-1<= 9:
                    for i in range(x+1, x+size):
                        poss_for_ship.append([i, y])
                else:
                    continue
            case 4:
                if x-size+1>= 0:
                    for i in range(x-size+1, x):
                        poss_for_ship.append([i, y])
                else:
                    continue

        if check_area_for_dots(poss_for_ship):
            for pos in poss_for_ship:
                filed_with_ships[pos[1]][pos[0]] = '1'
            ships_cords.append(poss_for_ship)
            putted += 1
     
def put_ships_on_map():
    put_ship(1, 4)
    put_ship(2, 3)
    put_ship(3, 2)
    put_ship(4, 1)


def show_map(field: list):
    field_for_show = '\n'
    first_row = ' 0 | 1 2 3 4 5 6 7 8 9 10 \n'
    second_row ='---+---------------------- \n' 
    field_for_show+= first_row
    field_for_show+= second_row
    for index, row in enumerate(field):
        row = ' '.join(row)
        if index+1 < 10:
            field_for_show += (rf' {index+1} | {row}' +'\n')
        else:
            field_for_show += (rf'{index+1} | {row}' +'\n')

    print(field_for_show)

def show_instruction():
    print("\nИнструкция!\n---------------------------------------------------------------------------------------------------------------------------------------------\nПрограмма автоматически случайно расставляет на поле размером 10 на 10 клеток: четыре однопалубных корабля, три двухпалубных корабля, два трехпалубных корабля и один четырехпалубный. Между любыми двумя кораблями по горизонтали и вертикали должна быть как минимум одна незанятая клетка. Программа позволяет игроку ходить, производя выстрелы. Сама программа НЕ ходит, т.е. не пытается топить корабли расставленные игроком. Взаимодействие с программой производится через консоль.\n---------------------------------------------------------------------------------------------------------------------------------------------")

def check_for_dead():
    for ship_cords in ships_cords:
        count = 0
        for coord in ship_cords:
            if field_with_hide_ships[coord[1]][coord[0]] == '*':
                count += 1
        if count == len(ship_cords):
            for x_dot, y_dot in ship_cords:
                left_pos = x_dot-1 if x_dot-1>=0 else 0
                right_pos = x_dot+1 if x_dot+1 <= 9 else 9
                top_pos = y_dot-1 if y_dot-1 >= 0 else 0
                bottom_pos = y_dot+1 if y_dot+1 <= 9 else 9

                for x in range(left_pos, right_pos+1):
                    for y in range(top_pos, bottom_pos+1):
                        field_with_hide_ships[y][x] = 'x'
            for coord in ship_cords:
                field_with_hide_ships[coord[1]][coord[0]] = '='
            ships_dead_cords.append(ship_cords)
    if sorted(ships_cords) == sorted(ships_dead_cords):
        print('Вы победили!!!!')
        exit()
    

def main():
    put_ships_on_map()
    show_instruction()
    print('\nЧтобы остановить игру напишите вместо координат "quit"\n')
    print('\nВот ваша изначальная карта!')
    show_map(field_with_hide_ships)
    input_txt = ''
    while True:
        input_txt = input('Введите координаты по которым хотите нанести удар в формате: x y (через пробел): ')
        if input_txt == 'quit':
            break
        else:
            try:
                x, y = [int(x)-1 for x in input_txt.split()]

                if filed_with_ships[y][x] == '1':
                    field_with_hide_ships[y][x] = '*'
                else:
                    field_with_hide_ships[y][x] = 'x'
                check_for_dead()
                show_map(field_with_hide_ships)
            except Exception as e:
                print('Неверный формат ввода. Повторите попытку в формате "x y"')
                print(e)


if __name__ == '__main__':
    main()