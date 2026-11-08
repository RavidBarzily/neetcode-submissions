class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0 
        j = len(s) - 1
        while i < j:
            print(i,j)
            while i < j and not s[i].isalnum():
                i += 1
            while j >= 0 and not s[j].isalnum():
                j -= 1
            if s[i].isalnum() and s[j].isalnum() and s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True