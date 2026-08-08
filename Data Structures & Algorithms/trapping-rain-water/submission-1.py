class Solution:
    def trap(self, height: List[int]) -> int:
        
        n = len(height)
        prefix = [-1] * n 
        suffix = [-1] * n
        maxN = height[0]

        for i in range(n):
            maxN = max(maxN, height[i])
            prefix[i] = maxN

        maxN = height[n-1]
        for j in range(n-1, -1, -1):
            maxN = max(maxN, height[j])
            suffix[j] = maxN
            
        trapped = 0
        for i in range(n):
            trapped += (min(prefix[i], suffix[i]) - height[i])

        return trapped