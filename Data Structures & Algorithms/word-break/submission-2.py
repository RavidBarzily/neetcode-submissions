class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[-1] = True
        lengths = {len(w) for w in wordDict}

        for i in reversed(range(len(dp))):
            curr = False
            for j in reversed(range(i, len(dp))):
                if j - i in lengths:
                    word = s[i:j]
                    if word in wordDict and dp[j]:
                        curr = True
            dp[i] = dp[i] or curr
    
        return dp[0]