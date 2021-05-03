from exceptions import BoardException, BoardWrongShipException
from inner_logic import Board, Dot, Ship, N
from random import randint


class Player:
    def __init__(self, user_board, ai_board):
        self.user_board = user_board
        self.ai_board = ai_board

    def ask(self):
        raise NotImplementedError()

    def move(self):
        while True:
            try:
                target = self.ask()
                repeat = self.ai_board.shot(target)
                return repeat
            except BoardException as e:
                print(e)


class AI(Player):
    def ask(self):
        dot = Dot(randint(0, N), randint(0, N))
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
    def __init__(self, size=N):
        self.size = size
        player = self.random_board()
        ai = self.random_board()
        ai.hid = True

        self.ai = AI(ai, player)
        self.user = User(player, ai)

    def random_board(self):
        board = None
        while board is None:
            board = self.random_place()
        return board

    def random_place(self):
        lens = [3, 2, 2, 1, 1, 1, 1]
        board = Board(size=self.size)
        attempts = 0
        for l in lens:
            while True:
                attempts += 1
                if attempts > 2000:
                    return None
                ship = Ship(Dot(randint(0, N), randint(0, N)), l, randint(0, 1))
                try:
                    board.add_ship(ship)
                    break
                except BoardWrongShipException:
                    pass
        board.begin()
        return board

    @staticmethod
    def greet():
        print("Игрок, привествую тебя в игре Морской Бой!")
        print("Формат ввода координат: x - номер строки, y - номер столбца.")

    def loop(self):
        num = 0
        while True:
            print("-" * 20)
            print("Доска пользователя:")
            print(self.user.user_board)
            print("-" * 20)
            print("Доска компьютера:")
            print(self.ai.ai_board)
            if num % 2 == 0:
                print("-" * 20)
                print("Ходит пользователь!")
                repeat = self.user.move()
            else:
                print("-" * 20)
                print("Ходит компьютер!")
                repeat = self.ai.move()
            if repeat:
                num -= 1

            if self.ai.ai_board.count == 7:
                print("-" * 20)
                print("Пользователь выиграл!")
                break

            if self.user.user_board.count == 7:
                print("-" * 20)
                print("Компьютер выиграл!")
                break
            num += 1

    def start(self):
        self.greet()
        self.loop()

