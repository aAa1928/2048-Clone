from pprint import pp
from random import randint

class Board:
    def __init__(self):
        self.grid = [[randint(0, 4) for _ in range(4)] for _ in range(4)]