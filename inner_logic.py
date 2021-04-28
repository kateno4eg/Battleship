class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def _eq_(self):
        return True


class Ship:
    def __init__(self, length, dot, direction, lives):
        self.length = length
        self.dot = dot
        self.direction = direction
        self.lives = lives

    def dots(self):
        return True


class Board:
    def __init__(self, grid, ship_list, hid, ship_balance):
        self.grid = grid
        self.ship_list = ship_list
        self.hid = hid
        self.ship_balance = ship_balance

    def add_ship(self):
        return True

    def contour(self):
        return True

    def out(self):
        return True

    def shot(self):
        return True





