class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = 0
        slowest = 0
        for pos, spe in sorted(zip(position, speed), reverse=True):
            t = (target - pos) / spe
            if t > slowest:
                fleets += 1
                slowest = t
        return fleets