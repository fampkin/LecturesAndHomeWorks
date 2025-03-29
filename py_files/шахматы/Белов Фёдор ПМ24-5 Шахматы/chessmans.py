letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
numbers = list(range(0, 8))

class ChessPiece:
    def __init__(self, color, letter, number, field, name):
        self.name = name
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
            print(f'Новая позиция {self.pos}')
            self.field.update()
            return True
        else:
            print('Неверная позиция, попробуйте снова')
            return False

    def get_position_indices(self, pos):
        letter = pos.get('letter')
        number = pos.get('number')
        return letters.index(letter), numbers.index(number)

    def calculate_move_differences(self, future_pos):
        index_future_letter, index_future_number = self.get_position_indices(future_pos)
        index_current_letter, index_current_number = self.get_position_indices(self.pos)
        
        return (
            abs(index_future_letter - index_current_letter),
            abs(index_future_number - index_current_number),
            index_future_number - index_current_number,
            index_future_letter,
            index_future_number,
            index_current_letter,
            index_current_number
        )

    def check_step(self, future_pos):
        raise NotImplementedError("Каждая фигура должна реализовать свою логику проверки хода")

class King(ChessPiece):
    def __init__(self, color, letter, number, field):
        super().__init__(color, letter, number, field, 'k')
        
    def check_step(self, future_pos):
        try:
            diff_letters, diff_numbers, _, _, future_number, _, _ = self.calculate_move_differences(future_pos)
            future_letter = future_pos.get('letter')
            
            return diff_letters <= 1 and diff_numbers <= 1 and (diff_letters != 0 or diff_numbers != 0) and \
                future_letter in letters and future_number in numbers and \
                (self.field.check_place(future_pos) or self.field.check_enemy(self.color, future_pos))
        except Exception as e:
            print(f'Ошибка при проверке хода короля {self.color}: {e}')
            return False

class Pawn(ChessPiece):
    def __init__(self, color, letter, number, field):
        super().__init__(color, letter, number, field, 'p')

    def check_step(self, future_pos):
        try:
            diff_letters, _, diff_numbers, _, _, _, current_number = self.calculate_move_differences(future_pos)
            current_letter = self.pos.get('letter')

            if self.color == 'белые':
                return self._check_white_pawn_move(diff_letters, diff_numbers, current_number, current_letter, future_pos)
            else:
                return self._check_black_pawn_move(diff_letters, diff_numbers, current_number, current_letter, future_pos)
        except Exception as e:
            print(f'Ошибка при проверке хода пешки {self.color}: {e}')
            return False

    def _check_white_pawn_move(self, diff_letters, diff_numbers, current_number, current_letter, future_pos):
        return (
            (diff_letters == 0 and diff_numbers == 1 and self.field.check_place(future_pos)) or
            (diff_letters == 1 and diff_numbers == 1 and self.field.check_enemy(self.color, future_pos)) or
            (diff_letters == 0 and diff_numbers == 2 and current_number == 1 and
             self.field.check_place({'letter': current_letter, 'number': current_number + 1}) and
             self.field.check_place(future_pos))
        )

    def _check_black_pawn_move(self, diff_letters, diff_numbers, current_number, current_letter, future_pos):
        return (
            (diff_letters == 0 and diff_numbers == -1 and self.field.check_place(future_pos)) or
            (diff_letters == 1 and diff_numbers == -1 and self.field.check_enemy(self.color, future_pos)) or
            (diff_letters == 0 and diff_numbers == -2 and current_number == 6 and
             self.field.check_place({'letter': current_letter, 'number': current_number - 1}) and
             self.field.check_place(future_pos))
        )

class Knight(ChessPiece):
    def __init__(self, color, letter, number, field):
        super().__init__(color, letter, number, field, 'n')

    def check_step(self, future_pos):
        try:
            diff_letters, diff_numbers, *_ = self.calculate_move_differences(future_pos)
            
            return ((diff_letters == 2 and diff_numbers == 1) or \
                (diff_letters == 1 and diff_numbers == 2)) and \
                (self.field.check_place(future_pos) or self.field.check_enemy(self.color, future_pos))
        except Exception as e:
            print(f'Ошибка при проверке хода коня {self.color}: {e}')
            return False

class Queen(ChessPiece):
    def __init__(self, color, letter, number, field):
        super().__init__(color, letter, number, field, 'q')

    def check_step(self, future_pos):
        try:
            diff_letters, diff_numbers, *_ = self.calculate_move_differences(future_pos)
            
            return (diff_letters == diff_numbers or diff_letters == 0 or diff_numbers == 0) and \
                self.field.check_path_clear(self.pos, future_pos) and \
                (self.field.check_place(future_pos) or self.field.check_enemy(self.color, future_pos))
        except Exception as e:
            print(f'Ошибка при проверке хода ферзя {self.color}: {e}')
            return False

class Rook(ChessPiece):
    def __init__(self, color, letter, number, field):
        super().__init__(color, letter, number, field, 'r')

    def check_step(self, future_pos):
        try:
            _, _, _, index_future_letter, index_future_number, index_current_letter, index_current_number = \
                self.calculate_move_differences(future_pos)
            
            return (index_future_letter == index_current_letter or index_future_number == index_current_number) and \
                self.field.check_path_clear(self.pos, future_pos) and \
                (self.field.check_place(future_pos) or self.field.check_enemy(self.color, future_pos))
        except Exception as e:
            print(f'Ошибка при проверке хода ладьи {self.color}: {e}')
            return False

class Bishop(ChessPiece):
    def __init__(self, color, letter, number, field):
        super().__init__(color, letter, number, field, 'b')

    def check_step(self, future_pos):
        try:
            diff_letters, diff_numbers, *_ = self.calculate_move_differences(future_pos)
            
            return diff_letters == diff_numbers and \
                self.field.check_path_clear(self.pos, future_pos) and \
                (self.field.check_place(future_pos) or self.field.check_enemy(self.color, future_pos))
        except Exception as e:
            print(f'Ошибка при проверке хода слона {self.color}: {e}')
            return False
