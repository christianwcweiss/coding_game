import string
from enum import Enum
from typing import List
from typing import Tuple


class Direction(Enum):
    LEFT = "left"
    RIGHT = "right"
    UP = "up"
    DOWN = "down"


class Solution:
    @staticmethod
    def solve(n: int, board: List[str]) -> int:
        total = 0
        fill_char = chr(ord("A") - 1)
        board = [list(row) for row in board]

        def is_on_board(row: int, column: int) -> bool:
            return 0 <= row <= n - 1 and 0 <= column <= n - 1

        def coordinates_after_move(origin_x: int, origin_y: int, direction: Direction) -> Tuple[int, int]:
            if direction is Direction.LEFT:
                return origin_x - 1, origin_y
            if direction is Direction.RIGHT:
                return origin_x + 1, origin_y
            if direction is Direction.UP:
                return origin_x, origin_y - 1
            if direction is Direction.DOWN:
                return origin_x, origin_y + 1

        for c in string.ascii_uppercase:
            if c == "Z":
                continue

            for i in range(n):
                for j in range(n):
                    parsed_board = [[ord(c) - ord("A") + 1 for c in row] for row in board]
                    current_height = parsed_board[i][j]

                    if not is_on_board(i, j) or c != board[i][j]:
                        continue

                    connected_tiles = [(i, j)]
                    seen_tiles = {(i, j)}
                    min_neighbouring_height = ord("Z") - ord("A") + 1
                    while connected_tiles:
                        tile_x, tile_y = connected_tiles.pop()
                        for direction in list(Direction):
                            x, y = coordinates_after_move(origin_x=tile_x, origin_y=tile_y, direction=direction)
                            if not is_on_board(x, y):
                                min_neighbouring_height = -1
                                continue

                            height = parsed_board[x][y] - current_height
                            if height == 0:
                                if (x, y) not in seen_tiles:
                                    connected_tiles.append((x, y))
                                    seen_tiles.add((x, y))
                                continue

                            min_neighbouring_height = min(min_neighbouring_height, height)

                    for x, y in seen_tiles:
                        board[x][y] = (
                            chr(ord(c) + min_neighbouring_height) if min_neighbouring_height > 0 else fill_char
                        )

                    total += max(min_neighbouring_height, 0) * len(seen_tiles)

        return total
