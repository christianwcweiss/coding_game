from typing import List


class Solution:
    ABBREVIATIONS = {
        "sp": " ",
        "bS": "\\",
        "sQ": "'",
    }

    @staticmethod
    def solve(text_input: str) -> List[str]:
        lines = [[]]
        for item in text_input.split():
            if item == "nl":
                lines.append([])
            elif item[-2:] in Solution.ABBREVIATIONS:
                lines[-1].append(Solution.ABBREVIATIONS.get(item[-2:], "") * int(item[:-2]))
            else:
                lines[-1].append(item[-1:] * int(item[:-1]))

        return ["".join(line) for line in lines]
