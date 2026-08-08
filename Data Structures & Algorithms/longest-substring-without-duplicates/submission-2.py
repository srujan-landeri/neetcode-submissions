class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        processed = set()
        st = 0
        ed = 0
        maxC = 0

        while ed < len(s):
            while s[ed] in processed:
                processed.remove(s[st])
                st += 1

            processed.add(s[ed])
            ed += 1
            maxC = max(maxC, ed - st)

        return maxC