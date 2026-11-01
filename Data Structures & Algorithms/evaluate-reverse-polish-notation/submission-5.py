class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ['+','-','*','/']
        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            elif len(stack) >= 2 and token == operators[0]:
                stack.append(stack.pop() + stack.pop())
            elif len(stack) >= 2 and token == operators[1]:
                first = stack.pop()
                stack.append(stack.pop() - first)
            elif len(stack) >= 2 and token == operators[2]:
                stack.append(stack.pop() * stack.pop())
            elif len(stack) >= 2 and token == operators[3]:
                first = stack.pop()
                stack.append(int(stack.pop() / first))
        return sum(stack)