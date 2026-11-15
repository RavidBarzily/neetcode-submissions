class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for i,temp in enumerate(temperatures):
            if not stack or temp <= temperatures[stack[-1]]:
                stack.append(i)

            while stack and temp > temperatures[stack[-1]]:
                res[stack[-1]] = i - stack[-1]
                stack.pop()
            
            stack.append(i)
        
        return res
