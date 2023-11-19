import math
from typing import List
from typing import Tuple


class Solution:
    PRIMES = {3, 5, 7, 11, 13, 17}

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
        if p not in {3, 5, 7}:
            raise ValueError(f"p must be 3, 5 or 7, but was {p}")

        if p <= row:
            result = 1
            for number in [int(c) + 1 for c in "".join([str(c) for c in Solution.convert_base(row, p)])]:
                result *= number

            return row + 1 - result

        return 0

    @staticmethod
    def subdivisions(
        p: int,
        rows: int,
        columns: int,
        min_triangle_nodes: int,
        min_triangle_height: int,
        bottom_triangles: int,
        triangle_nodes: int,
        height: int,
    ) -> int:
        print(
            f"p: {p}, rows: {rows}, columns: {columns}, min_triangle_nodes: {min_triangle_nodes}, min_triangle_height: {min_triangle_height}, bottom_triangles: {bottom_triangles}, triangle_nodes: {triangle_nodes}, height: {height}"
        )
        if height >= rows:
            return triangle_nodes

        if bottom_triangles % p == 0:
            min_triangle_nodes *= sum(num for num in range(p + 1))
            min_triangle_height = height
        else:
            triangle_nodes += min_triangle_nodes * ((bottom_triangles % p) + 1)
            height += min_triangle_height

        bottom_triangles += 1
        bottom_triangles %= p

        return Solution.subdivisions(
            p=p,
            rows=rows,
            columns=columns,
            min_triangle_nodes=min_triangle_nodes,
            min_triangle_height=min_triangle_height,
            bottom_triangles=bottom_triangles,
            triangle_nodes=triangle_nodes,
            height=height,
        )

    @staticmethod
    def solve(p: int, rows: int, columns: int) -> int:
        smallest_triangle_nodes = Solution.number_of_nodes(p, columns)
        triangle_nodes = Solution.subdivisions(
            p=p,
            rows=rows,
            columns=columns,
            min_triangle_nodes=smallest_triangle_nodes,
            min_triangle_height=p,
            bottom_triangles=1,
            triangle_nodes=smallest_triangle_nodes,
            height=p,
        )

        return triangle_nodes
