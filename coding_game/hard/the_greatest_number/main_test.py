import main
import pytest


class TestSolution:
    @pytest.mark.parametrize(
        "n, characters, expected",
        [
            [8, "4 9 8 . 8 5 2 -", -2.45889],
            [9, "7 4 1 . 2 5 8 9 9", 9987542.1],
            [8, "- 7 7 8 8 6 5 1", -1567788],
            [9, "- 4 0 0 5 9 8 . 2", -0.024589],
            [8, "0 0 0 1 0 0 0 .", 100000],
            [9, "- 0 0 0 0 0 0 0 .", 0],
            [9, "1 2 3 4 5 6 7 8 9", 987654321],
        ],
    )
    def test_solve_method(self, n: int, characters: str, expected: float) -> None:
        result = main.Solution().solve(n=n, characters=characters)

        assert result == expected
