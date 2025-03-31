from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
numbers = list(range(0, 8))

@dataclass
class Position:
    letter: str
    number: int

    def to_indices(self) -> Tuple[int, int]:
        """Преобразует буквенно-цифровые координаты в индексы матрицы"""
        return letters.index(self.letter), numbers.index(self.number)

class Field:
    def __init__(self):
        self.field_matrix: List[List[str]] = [['.' for _ in range(8)] for _ in range(8)]
        self.chessmans_list = []
        
    def update(self):
        """Обновляет матрицу поля на основе текущих позиций фигур"""
        self.field_matrix = [['.' for _ in range(8)] for _ in range(8)]
        for chessman in self.chessmans_list:
            pos = Position(chessman.pos.get('letter'), chessman.pos.get('number'))
            index_letter, index_number = pos.to_indices()
            show_letter = chessman.name[0].upper() if chessman.color == 'белые' else chessman.name[0].lower()
            self.field_matrix[index_number][index_letter] = show_letter
            
    def _get_cell(self, pos: Position) -> str:
        """Получает значение клетки по позиции"""
        index_letter, index_number = pos.to_indices()
        return self.field_matrix[index_number][index_letter]
            
    def check_place(self, pos: Dict[str, any]) -> bool:
        """Проверяет, свободна ли указанная позиция"""
        position = Position(pos.get('letter'), pos.get('number'))
        return self._get_cell(position) == '.'
    
    def check_enemy(self, color: str, pos: Dict[str, any]) -> bool:
        """Проверяет, находится ли в указанной позиции фигура противника"""
        position = Position(pos.get('letter'), pos.get('number'))
        place = self._get_cell(position)
        
        if place == '.':
            return False
        
        return place.islower() if color == 'белые' else place.isupper()
    
    def check_path_clear(self, start_pos: Dict[str, any], end_pos: Dict[str, any]) -> bool:
        """Проверяет, свободен ли путь между двумя позициями"""
        start = Position(start_pos.get('letter'), start_pos.get('number'))
        end = Position(end_pos.get('letter'), end_pos.get('number'))
        
        start_letter, start_number = start.to_indices()
        end_letter, end_number = end.to_indices()

        step_letter = self._get_step(start_letter, end_letter)
        step_number = self._get_step(start_number, end_number)

        current_letter = start_letter + step_letter
        current_number = start_number + step_number
        
        while current_letter != end_letter or current_number != end_number:
            if self.field_matrix[current_number][current_letter] != '.':
                return False
            current_letter += step_letter
            current_number += step_number
        return True

    @staticmethod
    def _get_step(start: int, end: int) -> int:
        """Определяет направление движения"""
        if start == end:
            return 0
        return 1 if end > start else -1

    def remove_enemy(self, pos: Dict[str, any], color: str):
        """Удаляет фигуру противника с указанной позиции"""
        position = Position(pos.get('letter'), pos.get('number'))
        
        enemy = next(
            (chessman for chessman in self.chessmans_list
             if chessman.pos.get('letter') == position.letter and
             chessman.pos.get('number') == position.number and
             chessman.color != color),
            None
        )
        
        if enemy:
            self.chessmans_list.remove(enemy)
            print(f"Фигура {enemy.name} цвета {enemy.color} удалена с позиции {position.letter}{position.number + 1}")
    
    def check_kings(self) -> Tuple[bool, bool]:
        """Проверяет наличие королей на поле"""
        return (
            any(chessman.name == 'k' and chessman.color == 'белые' for chessman in self.chessmans_list),
            any(chessman.name == 'k' and chessman.color == 'черные' for chessman in self.chessmans_list)
        )
    
    def show(self):
        """Отображает текущее состояние поля"""
        print('\n   ' + ' '.join(letters))
        print()
        for i in range(7, -1, -1):
            row = ' '.join(self.field_matrix[i])
            print(f"{i+1}  {row}  {i+1}")
        print('\n   ' + ' '.join(letters))
        print()
