from inner_logic import Board


class Player:
    def __init__(self, user_board, ai_board):
        self.user_board = user_board
        self.ai_board = ai_board

    def ask(self):
        pass

    def move(self):
        Player.ask()
        Board.shot()
        return True


class AI(Player):
    def ask(self):
        return True


class User(Player):
    def ask(self):
        move = input("Введите координаты ракетного удара: ")


class Game:
    def __init__(self, user, user_board, ai, ai_board):
        self.user = user
        self.user_board = user_board
        self.ai = ai
        self.ai_board = ai_board

    def random_board(self):
        return True

    def greet(self):
        return print("""Игрок, привествую тебя в игре "Морской Бой"! Формат хода: как в Крестики-нолики""")

    def loop(self):
        return True

    def start(self):
        Game.greet()
        Game.loop()
