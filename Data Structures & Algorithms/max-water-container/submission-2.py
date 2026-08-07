class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        maxArea = -1
        st = 0
        ed = len(heights) - 1

        while ed > st:
            maxArea = max(maxArea, (ed - st) * min(heights[st], heights[ed]))    

            if heights[st] < heights[ed]:
                st += 1
            else:
                ed -= 1
        return maxArea