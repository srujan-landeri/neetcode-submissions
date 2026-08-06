class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        _set = set()
        for num in nums:
            _set.add(num)
        
        ml = 0
        for num in nums:
            temp = num
            l = 1

            if temp-1 in _set:
                continue
            
            while temp+1 in _set:
                temp+=1
                l += 1
            

            ml = max(ml, l)

        return ml