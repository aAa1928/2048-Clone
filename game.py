from pprint import pp
from random import randint
from types import NoneType
from typing import Literal, Union

class Board:
    def __init__(self, grid: Union[list[list[int]], NoneType] = None):
        self.grid = [[0 for _ in range(4)] for _ in range(4)] if grid is None else grid

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

    def _move_left(self, _grid: list[list[int]] = None):
        grid = self.grid if _grid is None else _grid

        new_grid = []

        for row in grid:
            row = [x for x in row if x != 0]
            
            i = 0
            while i < len(row) - 1:
                if row[i] == row[i + 1]:
                    row[i] *= 2
                    row.pop(i + 1)
                i += 1
            
            while len(row) < 4:
                row.append(0)
            
            new_grid.append(row)

        self.grid = new_grid
        
        return new_grid

    def _move_right(self):
        self.grid = [row[::-1] for row in self.grid]
        self.grid = self._move_left()
        self.grid = [row[::-1] for row in self.grid]

        return self.grid

    def _move_up(self):
        self._rotate_counterclockwise()
        self._move_left()
        self._rotate_clockwise()
        return self.grid

    def _move_down(self):
        self._rotate_clockwise()
        self._move_left()
        self._rotate_counterclockwise()
        return self.grid
    
    def rotate(self, direction: Literal['clockwise', 'counterclockwise']):
        match direction:
            case 'clockwise':
                return self._rotate_clockwise()
            case 'counterclockwise':
                return self._rotate_counterclockwise()
            
    def _rotate_clockwise(self):
        new_grid = []

        for col in range(4):
            new_row = []
            for row in range(3, -1, -1):
                new_row.append(self.grid[row][col])
            new_grid.append(new_row)

        self.grid = new_grid
        return self.grid
    
    def _rotate_counterclockwise(self):
        new_grid = []

        for col in range(3, -1, -1):
            new_row = []
            for row in range(4):
                new_row.append(self.grid[row][col])
            new_grid.append(new_row)

        self.grid = new_grid
        return self.grid

    def is_won(self) -> bool:
        for row in self.grid:
            if 2048 in row:
                return True
        return False

    def __iter__(self):
        return iter(self.grid)

    def __getitem__(self, index):
        return self.grid[index]

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.grid])

    def __repr__(self):
        return f"Board(grid={self.grid})"

    def __eq__(self, other):
        if not isinstance(other, Board):
            return False
        return self.grid == other.grid

    def __len__(self):
        return len(self.grid)

if __name__ == '__main__':
    board = Board([
        [2, 0, 0, 1], 
        [2, 0, 1, 2], 
        [3, 3, 0, 3], 
        [4, 4, 1, 4]])

    print('\n')
    print(board)
    print('\n')
    board._move_up()
    print('\n')
    print(board)