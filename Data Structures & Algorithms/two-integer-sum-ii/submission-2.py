class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        st = 0
        ed = len(nums)-1

        while st < ed:

            s = nums[st] + nums[ed]
            if s == target:
                return [st+1, ed+1]
            
            elif s > target:
                ed -= 1

            else:
                st += 1

            