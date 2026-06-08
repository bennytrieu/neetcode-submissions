class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numb = 1
        i = 0
        j = numb
        while i < len(nums):
            j = numb
            while j < len(nums):
                if nums[i] == nums[j]:
                    return True
                j+=1
            numb+=1
            i+=1
        return False