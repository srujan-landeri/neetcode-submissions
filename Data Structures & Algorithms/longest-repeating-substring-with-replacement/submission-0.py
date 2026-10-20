class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l = 0
        r = 0

        maxFreq = 0
        counter = [0] * 26

        ret = 0

        while r < len(s):

            ind = ord(s[r]) - ord('A')
            counter[ind] += 1
            maxFreq = max(maxFreq, counter[ind])

            while r - l + 1 - maxFreq > k:
                
                ind = ord(s[l]) - ord('A')
                counter[ind] -= 1
                maxFreq = max(counter)
                l += 1
                
            ret = max(ret, r - l + 1)
            r += 1

        return ret