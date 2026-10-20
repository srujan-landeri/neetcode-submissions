class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        windowSize = len(s1)

        l = 0
        r = 0

        while r < len(s2):

            if r - l + 1 == windowSize:
                if self.checkPermute(s1, s2[l:r+1]):
                    return True
                l += 1
            r += 1

        return False

    def checkPermute(self, s1, s2):
        return sorted(s1) == sorted(s2)