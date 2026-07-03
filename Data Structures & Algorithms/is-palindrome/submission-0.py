class Solution:
    def isPalindrome(self, s: str) -> bool:
        length = len(s) - 1
        i = 0
        s = s.lower()
        while i < length:
            if s[i] == s[length]:
                i+=1
                length-=1
            elif not s[i].isalnum():
                i+=1
            elif not s[length].isalnum():
                length-=1
            else:
                return False
        return True