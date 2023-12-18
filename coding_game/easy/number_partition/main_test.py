from typing import List

import main
import pytest


class TestSolution:
    @pytest.mark.parametrize(
        "n, expected",
        [
            [1, ["1"]],
            [2, ["2", "1 1"]],
            [3, ["3", "2 1", "1 1 1"]],
            [4, ["4", "3 1", "2 2", "2 1 1", "1 1 1 1"]],
            [5, ["5", "4 1", "3 2", "3 1 1", "2 2 1", "2 1 1 1", "1 1 1 1 1"]],
        ],
    )
    def test_solve_method(self, n: int, expected: List[str]) -> None:
        result = main.Solution().solve(n=n)

        assert result == expected
