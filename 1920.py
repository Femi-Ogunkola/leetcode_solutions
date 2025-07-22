from typing import List

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        sol = []
        for i in range(len(nums)):
            sol.append(nums[nums[i]])
        
        return sol
        