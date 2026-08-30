class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d = dict()
        l = 0
        count = Counter(s1)
        
        for r in range(len(s2)):
            d[s2[r]] = d.get(s2[r], 0) + 1
            window = r - l + 1

            if window > len(s1):
                d[s2[l]] = d.get(s2[l], 0) - 1
                if d[s2[l]] == 0:
                    d.pop(s2[l])
                l += 1
            
            if d == count:
                return True
        print(d)
        print(count)
        return False