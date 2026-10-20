class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        tracker = set()
        lt = 0
        rt = 0

        maxLength = 0
        localLength = 0

        while rt < len(s):
            
            while s[rt] in tracker:
                tracker.remove(s[lt])
                lt += 1
            
            tracker.add(s[rt])
            localLength = (rt - lt + 1)          
            maxLength = max(localLength, maxLength)
            rt += 1

        return maxLength