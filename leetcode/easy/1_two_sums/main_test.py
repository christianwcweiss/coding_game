from typing import List

import main
import pytest


class TestSolution:
    @pytest.mark.parametrize(
        "nums, target, expected", [[[2, 7, 11, 15], 9, [0, 1]], [[3, 2, 4], 6, [1, 2]], [[3, 3], 6, [0, 1]]]
    )
    def test_solve_method(self, nums: List[int], target: int, expected: List[int]) -> None:
        result = main.Solution().solve(nums=nums, target=target)

        assert result == expected
