class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        my_dict = dict()
        l = 0
        r = 0
        ans = 0
        while l <= r and r < len(s):
            my_dict[s[r]] = my_dict.get(s[r], 0) + 1
            window = r - l + 1
            if window - max(my_dict.values()) <= k:
                ans = max(ans, window)
                r += 1
            else:
                my_dict[s[l]] = my_dict.get(s[l], 0) - 1
                my_dict[s[r]] = my_dict.get(s[r], 0) - 1
                l += 1
        
        return ans
            
            