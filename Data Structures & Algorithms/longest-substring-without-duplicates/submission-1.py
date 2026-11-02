class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        best = 0
        for right in s:
            while right in seen:
                seen.discard(s[left])
                left += 1
            seen.add(right)
            best = max(best,len(seen))
        return best