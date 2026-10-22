from collections import deque
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        digits = deque(digits)
        carry = 1
        while i >= 0:
            digits[i] += carry
            carry = 0
            if digits[i] > 9:
                carry += 1 #digits[i] - 9
                digits[i] = 0
            i -= 1
        if carry != 0:
            digits.appendleft(1)
        return list(digits)