class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # [-1,-1,-4,0,1,2]
        #   i       j k
        #   s = 0
        nums = sorted(nums)
        res = set()
        for i in range(len(nums)-2):
            j = i + 1
            k = len(nums) - 1

            while k > j:
                s = nums[i] + nums[j] + nums[k]

                if s == 0:
                    res.add((nums[i], nums[j], nums[k]))
                    k -= 1
                    j += 1

                elif s > 0:
                    k -= 1

                else:
                    j += 1
        
        return list(res)