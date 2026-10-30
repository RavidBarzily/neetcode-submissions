class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for op in operations:
            if op not in "CD+":
                stack.append(int(op))
            if stack and op == 'C':
                stack.pop()
            elif op == 'D' and stack:
                stack.append(stack[-1]*2)
            elif op == '+' and len(stack) >= 2:
                stack.append(stack[-1] + stack[-2])
        sol = 0
        while stack:
            sol += stack.pop()
        return sol