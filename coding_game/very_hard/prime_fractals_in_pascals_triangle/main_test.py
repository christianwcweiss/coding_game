from typing import List

import main
import pytest

TEST_CASES_POWERS_OF_PRIME = [
    [3, 3, 3],  # 6
    [3, 9, 9],  # 36
    [3, 27, 27],  # 216
    [3, 81, 81],
    [3, 243, 243],
    [5, 5, 5],
    [5, 25, 25],
    [5, 125, 125],
    [5, 625, 625],
    [7, 7, 7],
    [7, 49, 49],
    [7, 343, 343],
    [11, 11, 11],
    [11, 121, 121],
    [11, 1331, 1331],
    [13, 13, 13],
    [13, 169, 169],
    [17, 17, 17],
    [17, 289, 289],
]
TEST_CASES_ROWS_EQUALS_COLUMNS = [
    [3, 5, 5],
    [3, 14, 14],
    [3, 64, 64],
    [3, 754, 754],
    [5, 8, 8],
    [5, 123, 123],
    [5, 456, 456],
    [7, 11, 11],
    [7, 43, 43],
    [7, 349, 349],
    [11, 12, 12],
    [11, 24, 24],
    [11, 890, 890],
    [13, 14, 14],
    [13, 200, 200],
    [13, 666, 666],
    [17, 18, 18],
    [17, 345, 345],
    [17, 789, 789],
]


class TestSolution:
    @pytest.mark.parametrize(
        "p, rows, columns",
        TEST_CASES_POWERS_OF_PRIME + TEST_CASES_ROWS_EQUALS_COLUMNS,
    )
    def test_solve_method(self, p: int, rows: int, columns: int) -> None:
        expected = main.Solution.solve_brute_force(p=p, rows=rows, columns=columns)

        result = main.Solution().solve(p=p, rows=rows, columns=columns)

        assert result == expected

    def test_number_of_nodes(self) -> None:
        for rows in range(1, 50):
            for columns in range(1, 50):
                pascal_triangle = main.Solution().create_pascal_triangle(rows=rows)
                nodes = sum(sum(1 for i, column in enumerate(row) if i < columns) for row in pascal_triangle)

                assert nodes == main.Solution().number_of_nodes(rows, columns)

    @pytest.mark.parametrize(
        "number, base, expected",
        [
            [5, 2, [1, 0, 1]],
            [4, 3, [1, 1]],
            [5, 3, [1, 2]],
            [6, 3, [2, 0]],
            [7, 5, [1, 2]],
            [20, 5, [4, 0]],
        ],
    )
    def test_base_conversion(self, number: int, base: int, expected: List[int]) -> None:
        result = main.Solution().convert_base(number=number, base=base)

        assert result == expected

    def test_lucas_theorem(self) -> None:
        triangle = main.Solution.create_pascal_triangle(100)
        for prime in main.PRIMES:
            for i, row in enumerate(triangle):
                for j, column in enumerate(row):
                    assert main.Solution().lucas_theorem(p=prime, row=i, column=j) == bool(triangle[i][j] % prime == 0)

    @pytest.mark.parametrize("prime", [3, 5, 7, 11, 13, 17])
    def test_divisible_numbers_in_row(self, prime: int) -> None:
        triangle = main.Solution.create_pascal_triangle(100)
        for i, row in enumerate(triangle):
            assert main.Solution().divisible_numbers_in_row(p=prime, row=i) == sum(
                1 for number in row if number % prime == 0
            ), f"prime: {prime}, row: {i}, row: {row}"

    @pytest.mark.parametrize(
        "prime, expected",
        [
            [3, 40],
            [5, 28],
            [7, 23],
            [11, 19],
            [13, 18],
            [17, 16],
        ],
    )
    def test_iterations_of_max_rows_in_testcases(self, prime: int, expected: int) -> None:
        max_rows = main.MAX_ROWS
        iterations = 0

        while max_rows > 0:
            max_rows //= prime
            iterations += 1

        assert iterations == expected

    @pytest.mark.parametrize("p", main.PRIMES)
    def test_find_sizes_and_nodes(self, p: int) -> None:
        sizes_and_nodes = main.Solution.find_triangle_sizes_and_nodes(p=p)

        print(sizes_and_nodes)
