class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        processed = dict()
        for ind, val in enumerate(nums):
            goal = target - val
            if goal in processed:
                return [processed[goal], ind]
            processed[val] = ind 

        return [-1, -1]