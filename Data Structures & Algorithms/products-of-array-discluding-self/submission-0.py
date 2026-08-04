class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # [1, 2, 4, 6]
        # [1, 1, 2, 8]
        # [48,24,6, 1]

        # [-1,  0, 1, 2, 3]
        # [ 1, -1, 0, 0, 0]
        # [ 0,  6, 6, 3, 1]

        prefix = [1] * len(nums)
        suffix = [1] * len(nums)

        prefix[1]  = nums[0]
        suffix[-2] = nums[-1]

        for i in range(2, len(nums)):
            prefix[i] = prefix[i-1] * nums[i-1]
        
        for i in range(len(nums)-2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]
        
        print(prefix)
        print(suffix)
        return_list = [suffix[i] * prefix[i] for i in range(len(nums))]
        return return_list
          