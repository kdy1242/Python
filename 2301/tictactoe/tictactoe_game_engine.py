class TictactoeGameEngine:
    def __init__(self):
        self.SIZE = 3
        self.board = list('.' * self.SIZE * self.SIZE)      # ['.', '.', '.', '.', '.', '.', '.', '.', '.']
        self.turn = 'X'

    def show_board(self):
        print(self.board)

    def set(self, row, col):
        pass

    def set_winner(self):
        # - 3줄
        # | 3줄
        # \
        # /
        return self.turn
        # 비기는 조건: 다 채워졌을때 위의것에 해당안됐을때: self.board 에 '.'이 없는 상테
        return 'd'      # draw

    def change_turn(self):
        # self.turn 'X'면 'O'로, 'O'면 'X'로 바꾸자
        pass


if __name__ == '__main__':
    game_engine = TictactoeGameEngine()
    game_engine.show_board()    # ...\n...\n...
    game_engine.set(3, 2)
    game_engine.show_board()    # ['.', '.', '.', '.', '.', '.', '.', 'X', '.']
    game_engine.set(3, 1)
    game_engine.set(3, 3)
    print(game_engine.set_winner())     # 'X'
    game_engine.change_turn()
    print(game_engine.turn)      # 'O'
