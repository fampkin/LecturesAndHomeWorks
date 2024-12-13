from chessmans import *
from play_field import Field
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']


class Chess():
    def __init__(self):
        self.field = Field()
        self.init_chessmans()
        self.current_turn = 'white'  # Начинаем с белых
        self.field.show()
        self.steps = 0

    def init_chessmans(self):
        self.king_w = King(color='white', letter='E', number=1, field=self.field)
        self.king_b = King(color='black', letter='E', number=8, field=self.field)
        self.pawns_w = [Pawn(color='white', letter=letter, number=2, field=self.field) for letter in letters]
        self.pawns_b = [Pawn(color='black', letter=letter, number=7, field=self.field) for letter in letters]
        self.knights_w = [Knight(color='white', letter=letter, number=1, field=self.field) for letter in ['B', 'G']]
        self.knights_b = [Knight(color='black', letter=letter, number=8, field=self.field) for letter in ['B', 'G']]
        self.queen_w = Queen(color='white', letter='D', number=1, field=self.field)
        self.queen_b = Queen(color='black', letter='D', number=8, field=self.field)
        self.rooks_w = [Rook(color='white', letter=letter, number=1, field=self.field) for letter in ['A', 'H']]
        self.rooks_b = [Rook(color='black', letter=letter, number=8, field=self.field) for letter in ['A', 'H']]
        self.bishops_w = [Bishop(color='white', letter=letter, number=1, field=self.field) for letter in ['C', 'F']]
        self.bishops_b = [Bishop(color='black', letter=letter, number=8, field=self.field) for letter in ['C', 'F']]

    def start(self):
        while True:
            try:
                white_king, black_king = self.field.check_kings()
                if not white_king or not black_king:
                    print("Game over!")
                    if not white_king:
                        print("Black wins!")
                    elif not black_king:
                        print("White wins!")
                    break
                
                self.field.show()
                print(f'steps {self.steps}')
                print(f"{self.current_turn.capitalize()}'s turn")
                from_letter = input("Enter the letter of the piece to move: ").upper()
                from_number = int(input("Enter the number of the piece to move: "))
                to_letter = input("Enter the target letter: ").upper()
                to_number = int(input("Enter the target number: "))

                selected_chessman = self.chessman(from_letter, from_number)
                if not selected_chessman:
                    print("No piece found at the given position.")
                    continue

                if selected_chessman.color != self.current_turn:
                    print(f"It's {self.current_turn}'s turn!")
                    continue

                if selected_chessman.go_to(to_letter, to_number):
                    self.steps += 1
                    self.current_turn = 'black' if self.current_turn == 'white' else 'white'
            except Exception as e:
                print('Not correct void')
    
        

    def chessman(self, letter, number):
        for piece in self.field.chessmans_list:
            if piece.pos['letter'] == letter and piece.pos['number'] == number - 1:
                return piece
        return None

if __name__ == '__main__':
    chess = Chess()
    chess.start()