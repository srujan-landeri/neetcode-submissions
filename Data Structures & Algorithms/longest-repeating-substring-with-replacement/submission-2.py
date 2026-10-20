class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        maxFreq = 0
        ret = 0
        l = 0
        r = 0
        counter = [0] * 26

        while r < len(s):

            ind = ord(s[r]) - ord('A')
            counter[ind] += 1
            maxFreq = max(counter[ind], maxFreq)
            
            if r - l + 1 - maxFreq > k:

                ind = ord(s[l]) - ord('A')
                counter[ind] -= 1
                l += 1

            ret = max(ret, r - l + 1)
            r += 1 

        return ret     