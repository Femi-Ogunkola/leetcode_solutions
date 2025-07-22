
from itertools import combinations
from typing import List

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        ans = 0
        subsets = []
        for i in range(1, len(nums)+1):
            subsets += (list(combinations(nums, i)))

        for subset in subsets:
            s_a = 0
            # print('subset',subset, len(subset))
            if len(subset) == 1:
                ans += subset[0]
            else:
                for i in subset:
                    # print(i)
                    s_a ^= i
                ans += s_a

        return ans 