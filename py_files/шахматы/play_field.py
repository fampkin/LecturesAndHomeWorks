letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
numbers = list(range(0, 8))

class Field():
    def __init__(self):
        self.field_matrix = [['.' for _ in range(8)] for _ in range(8)]
        self.chessmans_list = []
        
    def update(self):
        self.field_matrix = [['.' for _ in range(8)] for _ in range(8)]
        for chessman in self.chessmans_list:
            letter = chessman.pos.get('letter')
            number = chessman.pos.get('number')
            index_letter = letters.index(letter)
            index_number = numbers.index(number)
            if chessman.color == 'white':
                show_letter = chessman.name[0].upper()
            else:
                show_letter = chessman.name[0].lower()
            self.field_matrix[index_number][index_letter] = show_letter  
            
    def check_place(self, pos):
        letter = pos.get('letter')
        number = pos.get('number')
        index_letter = letters.index(letter)
        index_number = numbers.index(number)
        return self.field_matrix[index_number][index_letter] == '.'
    
    def check_enemy(self, color, pos):
        letter = pos.get('letter')
        number = pos.get('number')
        index_letter = letters.index(letter)
        index_number = numbers.index(number)
        
        place = self.field_matrix[index_number][index_letter] 
        
        if place == '.':
            return False
        
        if color == 'white':
            return place.islower()
        elif color == 'black':
            return place.isupper()
    
    def check_path_clear(self, start_pos, end_pos):
        start_letter = start_pos.get('letter')
        start_number = start_pos.get('number')
        end_letter = end_pos.get('letter')
        end_number = end_pos.get('number')

        index_start_letter = letters.index(start_letter)
        index_start_number = numbers.index(start_number)
        index_end_letter = letters.index(end_letter)
        index_end_number = numbers.index(end_number)

        step_letter = 0 if index_start_letter == index_end_letter else (1 if index_end_letter > index_start_letter else -1)
        step_number = 0 if index_start_number == index_end_number else (1 if index_end_number > index_start_number else -1)

        current_letter = index_start_letter + step_letter
        current_number = index_start_number + step_number
        while current_letter != index_end_letter or current_number != index_end_number:
            if self.field_matrix[current_number][current_letter] != '.':
                return False
            current_letter += step_letter
            current_number += step_number
        return True

    def remove_enemy(self, pos, color):
        letter = pos.get('letter')
        number = pos.get('number')
        index_letter = letters.index(letter)
        index_number = numbers.index(number)

        for chessman in self.chessmans_list:
            if (
                chessman.pos.get('letter') == letter and
                chessman.pos.get('number') == number and
                chessman.color != color
            ):
                self.chessmans_list.remove(chessman)
                print(f"{chessman.name} of {chessman.color} removed from {letter}{number + 1}")
                break
    
    def check_kings(self):
        white_king = any(chessman.name == 'k' and chessman.color == 'white' for chessman in self.chessmans_list)
        black_king = any(chessman.name == 'k' and chessman.color == 'black' for chessman in self.chessmans_list)
        return white_king, black_king
    
    
    def show(self):
        print(' ')
        print("   " + " ".join(letters))  
        print(' ')
        for i in range(7, -1, -1): 
            row = " ".join(self.field_matrix[i])
            print(f"{i+1}  {row}  {i+1}")
        print(' ')
        print("   " + " ".join(letters))   
        print(' ')
