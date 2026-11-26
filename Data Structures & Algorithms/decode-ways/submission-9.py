class Solution:
    def numDecodings(self, s: str) -> int:  
        prev2 = 1
        prev1 = 1 if s[0] != '0' else 0
        for i in range(1, len(s)):
            curr = 0
            if s[i] != '0':
                curr += prev1
            if s[i - 1 : i + 1] < '27' and s[i - 1] != '0':
                curr += prev2
            prev2, prev1 = prev1, curr

        return prev1