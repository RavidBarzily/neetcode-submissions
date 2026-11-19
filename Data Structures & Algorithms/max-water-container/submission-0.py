class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights) - 1
        sol = 0
        while i < j:
            sol = max(sol,(j - i)*min(heights[i],heights[j]))
            if heights[i] < heights[j]:
                i += 1
            elif heights[i] == heights[j] :
                j -= 1
                i += 1
            else:
                j -= 1
        
        return sol