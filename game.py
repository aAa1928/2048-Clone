from pprint import pp
from random import randint
from typing import Literal

class Board:
    def __init__(self):
        self.grid = [[randint(0, 4) for _ in range(4)] for _ in range(4)]

    def pp(self):
        for row in self.grid:
            print(row)

    def add_tile(self):
        raise NotImplementedError("add_tile method not implemented") # TODO
    
    def move(self, direction: Literal['up', 'down', 'left', 'right']):
        match direction:
            case 'left':
                return self._move_left()
            case 'right':
                return self._move_right()
            case 'up':
                return self._move_up()
            case 'down':
                return self._move_down()

    def _move_left(self):
            new_grid = []

            for row in self.grid:
                if row == [0, 0, 0, 0]:
                    new_grid.append(row)
                    continue
                while row[0] == 0:
                    new_grid.append(row.pop(0))
                for i in range(0, len(row) - 1):
                    if row[i] == row[i + 1]:
                        row[i] *= 2
                        row.pop(i + 1)
                        row.append(0)
                
                new_grid.append(row)

            self.grid = new_grid
            
            return new_grid

    def _move_right(self):
        self.grid = [row[::-1] for row in self.grid]
        self.grid = self._move_left()

        return self.grid

    def _move_up(self):
        # Logic to move tiles up
        pass

    def _move_down(self):
        # Logic to move tiles down
        pass

    def _reverse(self):
        raise NotImplementedError("_reverse method not implemented") # TODO
    
    def rotate(self, direction: Literal['left', 'right']):
        match direction:
            case 'left':
                return self._rotate_left()
            case 'right':
                return self._rotate_right()
            
    def _rotate_left(self):
        raise NotImplementedError("_rotate_left method not implemented") # TODO
    
    def _rotate_right(self):
        raise NotImplementedError("_rotate_right method not implemented")

    def is_won(self) -> bool:
        for row in self.grid:
            if 2048 in row:
                return True
        return False

if __name__ == '__main__':
    pass