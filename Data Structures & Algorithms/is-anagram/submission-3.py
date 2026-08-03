class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        mapA = dict()
        mapB = dict()

        for i in range(len(s)):
            mapA[s[i]] = mapA.get(s[i], 0) + 1
            mapB[t[i]] = mapB.get(t[i], 0) + 1

        for k,v in mapA.items():
            if mapB.get(k, 0) == 0 or mapB.get(k, 0) != mapA[k]:
                return False
        
        return True