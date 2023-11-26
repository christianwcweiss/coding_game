import math
from typing import List
from typing import Optional
from typing import Tuple


PRIMES = {3, 5, 7, 11, 13, 17}
MAX_ROWS = 10**19


class Solution:
    @staticmethod
    def solve_brute_force(p: int, rows: int, columns: int) -> int:
        triangle = Solution.create_pascal_triangle(rows)
        nodes = 0
        for row in triangle:
            for i, column in enumerate(row):
                if i >= columns:
                    break
                if column % p != 0:
                    nodes += 1

        return nodes

    @staticmethod
    def find_triangle_sizes_and_nodes(p: int) -> List[Tuple[int, int]]:
        s = sum(i for i in range(p + 1))
        sizes = [(s, p)]  # (nodes, height)
        while sizes[-1][1] <= MAX_ROWS:
            sizes.append((sizes[-1][0] * s, sizes[-1][1] * p))

        return sizes

    @staticmethod
    def create_pascal_triangle(rows: int) -> List[List[int]]:
        triangle = []

        for row in range(1, rows + 1):
            if row == 1:
                triangle.append([1])
            elif row == 2:
                triangle.append([1, 1])
            else:
                triangle.append(
                    [1] + [triangle[-1][i] + triangle[-1][i + 1] for i in range(len(triangle[-1]) - 1)] + [1]
                )

        return triangle

    @staticmethod
    def _faculty(n: int) -> int:
        if n == 1:
            return 1

        return n * Solution._faculty(n - 1)

    @staticmethod
    def gauss_sum_formula(n: int) -> int:
        return (n * n + n) // 2

    @staticmethod
    def number_of_nodes(rows: int, columns: int) -> int:
        full_rows = min(rows, columns)
        nodes = Solution.gauss_sum_formula(full_rows)
        if rows > columns:
            nodes += (rows - full_rows) * columns

        return nodes

    @staticmethod
    def convert_base(number: int, base: int) -> List[int]:
        digits = []
        while number:
            digits.append(number % base)
            number //= base

        return digits[::-1]

    @staticmethod
    def lucas_theorem(p: int, row: int, column: int) -> bool:
        converted_row = Solution.convert_base(row, p)
        converted_column = Solution.convert_base(column, p)
        if len(converted_row) > len(converted_column):
            converted_column = [0 for _ in range(len(converted_row) - len(converted_column))] + converted_column
        elif len(converted_row) < len(converted_column):
            converted_row = [0 for _ in range(len(converted_column) - len(converted_row))] + converted_row

        return any(digit_1 < digit_2 for digit_1, digit_2 in zip(converted_row, converted_column))

    @staticmethod
    def divisible_numbers_in_row(p: int, row: int) -> int:
        if row >= p:
            result = 1
            converted_base = Solution.convert_base(row, p)
            for number in [base + 1 for base in converted_base]:
                result *= number

            return row + 1 - result

        return 0

    @staticmethod
    def subdivisions(
        p: int,
        rows: int,
        max_rows: int,
        total_nodes: int,
        iteration: int,
        sizes_and_nodes: List[Tuple[int, int]],
        last_size: Optional[int] = None,
        size_has_changed: bool = True,
    ) -> int:
        if rows == 0:
            return total_nodes

        if rows < p or not size_has_changed:
            nodes_in_row = (max_rows - rows + 1) - Solution.divisible_numbers_in_row(p=p, row=max_rows - rows)
            total_nodes += nodes_in_row
            return Solution.subdivisions(
                p=p,
                rows=rows - 1,
                max_rows=max_rows,
                total_nodes=total_nodes,
                iteration=iteration,
                sizes_and_nodes=sizes_and_nodes,
                last_size=last_size,
                size_has_changed=size_has_changed,
            )

        nodes, size = [(nodes, size) for nodes, size in sizes_and_nodes if size <= rows][-1]
        if size == last_size:
            return Solution.subdivisions(
                p=p,
                rows=rows,
                max_rows=max_rows,
                total_nodes=total_nodes,
                iteration=iteration,
                sizes_and_nodes=sizes_and_nodes,
                last_size=last_size,
                size_has_changed=False,
            )

        total_nodes += nodes * iteration

        return Solution.subdivisions(
            p=p,
            rows=rows - size,
            max_rows=max_rows,
            total_nodes=total_nodes,
            iteration=iteration + 1,
            sizes_and_nodes=sizes_and_nodes,
            last_size=size,
            size_has_changed=size != last_size,
        )

    @staticmethod
    def solve(p: int, rows: int, columns: int) -> int:
        sizes_and_nodes = Solution.find_triangle_sizes_and_nodes(p=p)

        return Solution.subdivisions(
            p=p,
            rows=rows,
            max_rows=rows,
            total_nodes=0,
            iteration=1,
            sizes_and_nodes=sizes_and_nodes,
            last_size=None,
            size_has_changed=True,
        )
