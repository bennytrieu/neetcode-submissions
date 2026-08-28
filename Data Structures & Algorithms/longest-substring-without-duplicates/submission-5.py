class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        arr = set()
        l = 0
        r = 0
        res = 0

        while r < len(s):
            if s[r] not in arr:
                arr.add(s[r])
                r+=1
                res = max(res, r - l)
            else:
                while s[r] in arr:
                    arr.remove(s[l])
                    l+=1
                
            
        return res