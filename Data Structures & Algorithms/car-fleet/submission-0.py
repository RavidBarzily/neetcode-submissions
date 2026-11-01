class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = list(zip(position, speed))   # [(0, 2), (4, 1), (2, 3)]
        pairs.sort(key=lambda p: p[0], reverse=True) # [(4, 1), (2, 3), (0, 2)]
        stack = []
        for pos, spd in pairs:
            if not stack:
                stack.append((target - pos) / spd)
            elif (target - pos) / spd > stack[-1]:
                stack.append((target - pos) / spd)
        return len(stack)