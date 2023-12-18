from typing import List


class Solution:
    @staticmethod
    def solve(n: int) -> List[str]:
        result = set()
        st = [([n - i], n - (n - i)) for i in range(n)]
        while st:
            l, remaining = st.pop()
            if remaining < 0:
                continue
            elif remaining == 0:
                result.add(" ".join(map(str, l)))
            else:
                for i in range(1, remaining + 1):
                    if i <= l[-1]:
                        st.append((l + [i], remaining - i))

        return sorted(result, reverse=True)
