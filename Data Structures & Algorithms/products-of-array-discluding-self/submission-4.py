class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # [1, 2, 4, 6]
        # [1, 1, 2, 8]

        # [48,24,12,8]

        # [-1,  0, 1, 2, 3]
        # [ 1, -1, 0, 0, 0]
        # [ 0,  6, 6, 3, 1]

        prefix = [1] * len(nums)
        suffix = [1] * len(nums)

        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] * nums[i-1]
        
        suffix = 1
        for i in range(len(nums)-2, -1, -1):
            suffix *= nums[i+1]
            prefix[i] *= suffix

        return prefix