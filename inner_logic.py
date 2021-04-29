N = 6
cruiser_number = 1
destroyer_number = 2
boat_number = 4
cruiser_length = 3
destroyer_length = 2
boat_length = 1


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
    def __init__(self, grid, ship_list, balance, hid=True):
        self.grid = grid
        self.ship_list = ship_list
        self.balance = balance
        self.hid = hid

# Метод ставит корабль на доску (если ставить не получается, выбрасываем исключения).
    def add_ship(self):
        return True

# Метод contour, который обводит корабль по контуру.
#  Он будет полезен и в ходе самой игры, и в при расстановке кораблей
#  (помечает соседние точки, где корабля по правилам быть не может).
    def contour(self):
        return True

# Метод, который выводит доску в консоль в зависимости от параметра hid.
    def print_out(self, hid):
        return True

# Метод out, который для точки (объекта класса Dot) возвращает True,
# если точка выходит за пределы поля, и False, если не выходит.
    def out(self):
        return True

# Метод shot, который делает выстрел по доске
# (если есть попытка выстрелить за пределы и в использованную точку, нужно выбрасывать исключения).
    def shot(self):
        return True





