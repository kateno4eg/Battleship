from inner_logic import Board, Dot, N
from random import randint


class Player:
    def __init__(self, user_board, ai_board):
        self.user_board = user_board
        self.ai_board = ai_board

    def ask(self):
        pass

    def move(self):
        self.ask()
        self.shot()
        return True


class AI(Player):
    def ask(self):
        dot = Dot(randint(range(N)), randint(range(N)))
        print(f'ИИ нанес вам ответный удар: {dot.x+1} {dot.y+1}')


class User(Player):
    def ask(self):
        while True:
            coordinates = input("Введите координаты ракетного удара: ").split()
            if len(coordinates) != 2:
                print("Неверный ввод: введите 2 координаты!")
                continue
            x, y = coordinates
            if not(x.isdigit()) or not(y.isdigit()):
                print("Неверный ввод: введите координаты в числовом формате!")
                continue
            x, y = int(x), int(y)
            return Dot(x-1, y-1)


class Game:
    def __init__(self, user, user_board, ai, ai_board):
        self.user = user
        self.user_board = user_board
        self.ai = ai
        self.ai_board = ai_board

    def random_board(self):
        empty_grid = [["O" for c in range(N)] for r in range(N)]
        grid = empty_grid
        return grid

    @staticmethod
    def greet():
        print("Игрок, привествую тебя в игре Морской Бой!")
        print("Формат ввода координат: x - номер строки, y - номер столбца.")

    def loop(self):
        return True

    def start(self):
        self.greet()
        self.loop()
