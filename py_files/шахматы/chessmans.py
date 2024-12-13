letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
numbers = list(range(0, 8))

class King():
    def __init__(self, color, letter, number, field):
        self.name = 'k'
        self.color = color
        self.field = field
        self.pos = {
            'letter': letter,
            'number': number-1
        }
        self.field.chessmans_list.append(self) 
        self.field.update()
        
        
    def go_to(self, letter, number):
        future_pos = {
            'letter': letter,
            'number': number-1
        }
        if self.check_step(future_pos):
            self.field.remove_enemy(future_pos, self.color)
            self.pos = future_pos
            print(f'New pos {self.pos}')
            self.field.update()
            self.field.show()
            return True
        else:
            self.field.show()
            print('Wrong pos, try again')
            return False
        
        
    def check_step(self, future_pos):
        try:
            future_letter = future_pos.get('letter')
            future_number = future_pos.get('number')
            index_future_letter = letters.index(future_letter)
            index_future_number = numbers.index(future_number)
            current_letter = self.pos.get('letter')
            current_number = self.pos.get('number')
            index_current_letter = letters.index(current_letter)
            index_current_number = numbers.index(current_number)
            diff_letters = abs(index_future_letter-index_current_letter)
            diff_numbers = abs(index_future_number-index_current_number)
            
            return diff_letters <=1 and diff_numbers <= 1 and (diff_letters != 0 or diff_numbers!=0) and \
                future_letter in letters and future_number in numbers and (self.field.check_place(future_pos) or self.field.check_enemy(self.color, future_pos))
        
        except Exception as e:
            print(f'Error with checking step for King {self.color}: {e}')
            return False
          
class Pawn():
    def __init__(self, color, letter, number, field):
        self.name = 'p'
        self.color = color
        self.field = field
        self.pos = {
            'letter': letter,
            'number': number - 1
        }
        self.field.chessmans_list.append(self)
        self.field.update()

    def go_to(self, letter, number):
        future_pos = {
            'letter': letter,
            'number': number - 1
        }
        if self.check_step(future_pos):
            self.field.remove_enemy(future_pos, self.color)
            self.pos = future_pos
            print(f'New pos {self.pos}')
            self.field.update()
            self.field.show()
            return True
        else:
            self.field.show()
            print('Wrong pos, try again')
            return False

    def check_step(self, future_pos):
        try:
            future_letter = future_pos.get('letter')
            future_number = future_pos.get('number')
            index_future_letter = letters.index(future_letter)
            index_future_number = numbers.index(future_number)
            current_letter = self.pos.get('letter')
            current_number = self.pos.get('number')
            index_current_letter = letters.index(current_letter)
            index_current_number = numbers.index(current_number)

            diff_letters = abs(index_future_letter - index_current_letter)
            diff_numbers = abs(index_future_number - index_current_number)

            diff_letters = abs(index_future_letter - index_current_letter)
            diff_numbers = index_future_number - index_current_number

            if self.color == 'white':
                valid_move = (
                    diff_letters == 0 and
                    diff_numbers == 1 and
                    self.field.check_place(future_pos)
                )
                valid_attack = (
                    diff_letters == 1 and
                    diff_numbers == 1 and
                    self.field.check_enemy(self.color, future_pos)
                )
                valid_double_move = (
                    diff_letters == 0 and
                    diff_numbers == 2 and
                    current_number == 1 and
                    self.field.check_place({'letter': current_letter, 'number': current_number + 1}) and
                    self.field.check_place(future_pos)
                )
                return valid_move or valid_attack or valid_double_move

            elif self.color == 'black':
                valid_move = (
                    diff_letters == 0 and
                    diff_numbers == -1 and
                    self.field.check_place(future_pos)
                )
                valid_attack = (
                    diff_letters == 1 and
                    diff_numbers == -1 and
                    self.field.check_enemy(self.color, future_pos)
                )
                valid_double_move = (
                    diff_letters == 0 and
                    diff_numbers == -2 and
                    current_number == 6 and
                    self.field.check_place({'letter': current_letter, 'number': current_number - 1}) and
                    self.field.check_place(future_pos)
                )
                return valid_move or valid_attack or valid_double_move 
        except Exception as e:
            print(f'Error with checking step for Pawn {self.color}: {e}')
            return False

class Knight():
    def __init__(self, color, letter, number, field):
        self.name = 'n'
        self.color = color
        self.field = field
        self.pos = {
            'letter': letter,
            'number': number - 1
        }
        self.field.chessmans_list.append(self)
        self.field.update()

    def go_to(self, letter, number):
        future_pos = {
            'letter': letter,
            'number': number - 1
        }
        if self.check_step(future_pos):
            self.field.remove_enemy(future_pos, self.color)
            
            self.pos = future_pos
            print(f'New pos {self.pos}')
            self.field.update()
            self.field.show()
            return True
        else:
            self.field.show()
            print('Wrong pos, try again')
            return False

    def check_step(self, future_pos):
        try:
            future_letter = future_pos.get('letter')
            future_number = future_pos.get('number')
            index_future_letter = letters.index(future_letter)
            index_future_number = numbers.index(future_number)
            current_letter = self.pos.get('letter')
            current_number = self.pos.get('number')
            index_current_letter = letters.index(current_letter)
            index_current_number = numbers.index(current_number)

            diff_letters = abs(index_future_letter - index_current_letter)
            diff_numbers = abs(index_future_number - index_current_number)

            return ((diff_letters == 2 and diff_numbers == 1) or \
                (diff_letters == 1 and diff_numbers == 2)) and (self.field.check_place(future_pos) or self.field.check_enemy(self.color, future_pos))


        except Exception as e:
            print(f'Error with checking step for Knight {self.color}: {e}')
            return False
    
class Queen():
    def __init__(self, color, letter, number, field):
        self.name = 'q'
        self.color = color
        self.field = field
        self.pos = {
            'letter': letter,
            'number': number - 1
        }
        self.field.chessmans_list.append(self)
        self.field.update()

    def go_to(self, letter, number):
        future_pos = {
            'letter': letter,
            'number': number - 1
        }
        if self.check_step(future_pos):
            self.field.remove_enemy(future_pos, self.color)
            
            self.pos = future_pos
            print(f'New pos {self.pos}')
            self.field.update()
            self.field.show()
            return True
        else:
            self.field.show()
            print('Wrong pos, try again')
            return False

    def check_step(self, future_pos):
        try:
            future_letter = future_pos.get('letter')
            future_number = future_pos.get('number')
            index_future_letter = letters.index(future_letter)
            index_future_number = numbers.index(future_number)
            current_letter = self.pos.get('letter')
            current_number = self.pos.get('number')
            index_current_letter = letters.index(current_letter)
            index_current_number = numbers.index(current_number)

            diff_letters = abs(index_future_letter - index_current_letter)
            diff_numbers = abs(index_future_number - index_current_number)

            return (diff_letters == diff_numbers or diff_letters == 0 or diff_numbers == 0) and \
                self.field.check_path_clear(self.pos, future_pos) and (self.field.check_place(future_pos) or self.field.check_enemy(self.color, future_pos))


        except Exception as e:
            print(f'Error with checking step for Queen {self.color}: {e}')
            return False
                
class Rook():
    def __init__(self, color, letter, number, field):
        self.name = 'r'
        self.color = color
        self.field = field
        self.pos = {
            'letter': letter,
            'number': number - 1
        }
        self.field.chessmans_list.append(self)
        self.field.update()

    def go_to(self, letter, number):
        future_pos = {
            'letter': letter,
            'number': number - 1
        }
        if self.check_step(future_pos):
            self.field.remove_enemy(future_pos, self.color)
            self.pos = future_pos
            print(f'New pos {self.pos}')
            self.field.update()
            self.field.show()
            return True
        else:
            self.field.show()
            print('Wrong pos, try again')
            return False

    def check_step(self, future_pos):
        try:
            future_letter = future_pos.get('letter')
            future_number = future_pos.get('number')
            index_future_letter = letters.index(future_letter)
            index_future_number = numbers.index(future_number)
            current_letter = self.pos.get('letter')
            current_number = self.pos.get('number')
            index_current_letter = letters.index(current_letter)
            index_current_number = numbers.index(current_number)

            return (index_future_letter == index_current_letter or index_future_number == index_current_number) and \
                self.field.check_path_clear(self.pos, future_pos) and (self.field.check_place(future_pos) or self.field.check_enemy(self.color, future_pos))
            

        except Exception as e:
            print(f'Error with checking step for Rook {self.color}: {e}')
            return False

class Bishop():
    def __init__(self, color, letter, number, field):
        self.name = 'Bishop'
        self.color = color
        self.field = field
        self.pos = {
            'letter': letter,
            'number': number - 1
        }
        self.field.chessmans_list.append(self)
        self.field.update()

    def go_to(self, letter, number):
        future_pos = {
            'letter': letter,
            'number': number - 1
        }
        if self.check_step(future_pos):
            self.field.remove_enemy(future_pos, self.color)
            self.pos = future_pos
            print(f'New pos {self.pos}')
            self.field.update()
            self.field.show()
            return True
        else:
            self.field.show()
            print('Wrong pos, try again')
            return False

    def check_step(self, future_pos):
        try:
            future_letter = future_pos.get('letter')
            future_number = future_pos.get('number')
            index_future_letter = letters.index(future_letter)
            index_future_number = numbers.index(future_number)
            current_letter = self.pos.get('letter')
            current_number = self.pos.get('number')
            index_current_letter = letters.index(current_letter)
            index_current_number = numbers.index(current_number)

            diff_letters = abs(index_future_letter - index_current_letter)
            diff_numbers = abs(index_future_number - index_current_number)
            
            return diff_letters == diff_numbers and self.field.check_path_clear(self.pos, future_pos) and (self.field.check_place(future_pos) or self.field.check_enemy(self.color, future_pos))

        except Exception as e:
            print(f'Error with checking step for Bishop {self.color}: {e}')
            return False
