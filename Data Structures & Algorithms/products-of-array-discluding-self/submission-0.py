class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr = []
        val = 1
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    val *= nums[j]
            arr.append(val)
            val = 1
        return arr