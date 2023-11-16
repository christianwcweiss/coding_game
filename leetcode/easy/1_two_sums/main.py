from typing import List


class Solution:
    @staticmethod
    def solve(nums: List[int], target: int) -> List[int]:
        complement_dictionary = {}
        for i, num in enumerate(nums):
            if num in complement_dictionary:
                return [complement_dictionary[num], i]
            complement_dictionary[target - num] = i
