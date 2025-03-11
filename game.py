from copy import deepcopy
from pprint import pp
from random import choice, random
from typing import Literal, Union, Optional, List

DirectionType = Literal['up', 'down', 'left', 'right']

class Board:
    def __init__(self, grid: Optional[List[List[int]]] = None, *, score: int = 0):
        """Initialize a new game board.
        
        Args:
            grid: Optional 2D list representing initial board state
        """
        self.score = score

        self._grid = [[0 for _ in range(4)] for _ in range(4)] if grid is None else grid
        if grid is None:
            for _ in range(2):
                self.add_tile()

    @property
    def grid(self) -> List[List[int]]:
        return self._grid
    
    @grid.setter
    def grid(self, value: List[List[int]]):
        self._grid = value

    def add_tile(self) -> List[List[int]]:
        """Add a new tile (2 or 4) to a random empty cell.
        
        Returns:
            The updated grid
        """
        empty_cells = [(i, j) for i in range(4) for j in range(4) if self.grid[i][j] == 0]
        if empty_cells:
            i, j = choice(empty_cells)
            self.grid[i][j] = 4 if random() < 0.1 else 2
        return self.grid
    
    def move(self, direction: DirectionType, *, add_tile: bool = True) -> List[List[int]]:
        """Move tiles in the specified direction.
        
        Args:
            direction: One of 'up', 'down', 'left', 'right'
            add_tile: Whether to add a new tile after the move
            
        Returns:
            The updated grid
        """
        init_grid = deepcopy(self.grid)

        match direction:
            case 'left':
                self._move_left()
            case 'right':
                self._move_right()
            case 'up':
                self._move_up()
            case 'down':
                self._move_down()
            case _:
                raise ValueError(f"Invalid direction: {direction}")
        
        if add_tile and init_grid != self.grid:
            self.add_tile()

        return self.grid

    def _move_left(self, _grid: list[list[int]] = None):
        grid = self.grid if _grid is None else _grid

        new_grid = []

        for row in grid:
            row = [x for x in row if x != 0]
            
            i = 0
            while i < len(row) - 1:
                if row[i] == row[i + 1]:
                    row[i] *= 2
                    self.score += row[i]
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
    
    def _rotate(self, direction: Literal['clockwise', 'counterclockwise']):
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
            if max(row) == 2048:
                return True
        return False
    
    def is_game_over(self) -> bool:
        for row in self.grid:
            if 0 in row:
                return False
        for i in range(4):
            for j in range(3):
                if self.grid[i][j] == self.grid[i][j + 1] or self.grid[j][i] == self.grid[j + 1][i]:
                    return False
        return True
    
    def flatten(self) -> List[int]:
        return [num for row in self.grid for num in row]

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
    pass