class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        numset = set()
        for i in nums:
            if i in numset:
                return i
            else:
                numset.add(i)