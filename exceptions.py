class BoardException(Exception):
    pass


class BoardOutException(BoardException):
    def __str__(self):
        return "Координаты удара вне расположения вражеских войск!"


class BoardUsedException(BoardException):
    def __str__(self):
        return "Два раза в одну воронку снаряд не попадает! Введите другие координаты"


class BoardWrongShipException(BoardException):
    pass
