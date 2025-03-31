from chessmans import *
from play_field import Field
from typing import Optional, List, Dict, Tuple

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

class Chess:
    def __init__(self):
        self._piece_positions: Dict[str, List[Tuple[str, int]]] = {
            'King': [('E', 1), ('E', 8)],
            'Pawn': [(letter, 2) for letter in letters] + [(letter, 7) for letter in letters],
            'Knight': [('B', 1), ('G', 1), ('B', 8), ('G', 8)],
            'Queen': [('D', 1), ('D', 8)],
            'Rook': [('A', 1), ('H', 1), ('A', 8), ('H', 8)],
            'Bishop': [('C', 1), ('F', 1), ('C', 8), ('F', 8)]
        }
        self.field = Field()
        self.init_chessmans()
        self.current_turn = 'белые'
        self.steps = 0
        

    def init_chessmans(self):
        """Инициализация шахматных фигур"""
        for piece_type, positions in self._piece_positions.items():
            for pos in positions:
                letter, number = pos
                color = 'белые' if number <= 2 else 'черные'
                piece_class = globals()[piece_type]
                piece = piece_class(color=color, letter=letter, number=number, field=self.field)
                setattr(self, f"{piece_type.lower()}_{color[0]}", piece)

    def _get_move_input(self) -> Tuple[str, int, str, int]:
        """Получение ввода для хода от пользователя"""
        try:
            from_letter = input("Введите букву фигуры для хода: ").upper()
            from_number = int(input("Введите номер фигуры для хода: "))
            to_letter = input("Введите букву целевой позиции: ").upper()
            to_number = int(input("Введите номер целевой позиции: "))
            return from_letter, from_number, to_letter, to_number
        except ValueError:
            raise ValueError("Неверный формат ввода")

    def _switch_turn(self):
        """Переключение хода между игроками"""
        self.current_turn = 'черные' if self.current_turn == 'белые' else 'белые'
        self.steps += 1

    def _check_game_over(self) -> bool:
        """Проверка окончания игры"""
        white_king, black_king = self.field.check_kings()
        if not white_king or not black_king:
            print("Игра окончена!")
            winner = "Черные" if not white_king else "Белые"
            print(f"{winner} победили!")
            print(f"Ходов: {self.steps}")
            return True
        return False

    def chessman(self, letter: str, number: int) -> Optional[ChessPiece]:
        """Поиск фигуры на доске по координатам"""
        return next(
            (piece for piece in self.field.chessmans_list 
             if piece.pos.get('letter') == letter and piece.pos.get('number') == number - 1),
            None
        )

    def start(self):
        """Основной игровой цикл"""
        while True:
            try:
                if self._check_game_over():
                    break

                self.field.show()
                print(f'Ходов: {self.steps}')
                print(f"Ход {self.current_turn}")

                from_letter, from_number, to_letter, to_number = self._get_move_input()
                selected_piece = self.chessman(from_letter, from_number)

                if not selected_piece:
                    print("Фигура не найдена на указанной позиции.")
                    continue

                if selected_piece.color != self.current_turn:
                    print(f"Сейчас ход {self.current_turn}!")
                    continue

                if selected_piece.go_to(to_letter, to_number):
                    self._switch_turn()

            except ValueError as e:
                print(f"Ошибка ввода: {e}")
            except Exception as e:
                print(f"Произошла ошибка: {e}")

if __name__ == '__main__':
    chess = Chess()
    chess.start()