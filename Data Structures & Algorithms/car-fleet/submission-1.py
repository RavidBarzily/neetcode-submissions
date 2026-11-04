class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position,speed))
        cars.sort(reverse = True)
        stack = []
        for pos,spe in cars:
            if not stack or (target - pos) / spe > stack[-1]:
                stack.append((target - pos) / spe)
        return len(stack)