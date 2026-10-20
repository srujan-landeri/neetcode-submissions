class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l = 0
        r = 0
        window = set()
        ret = 0
        
        while r < len(s):

            while s[r] in window:
                window.remove(s[l])
                l += 1
            
            window.add(s[r])
            ret = max(ret, r - l + 1)
            r += 1

        return ret