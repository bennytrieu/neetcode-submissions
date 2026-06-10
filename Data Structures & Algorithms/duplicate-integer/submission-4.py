class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # holder = 0

        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if (nums[j] < nums[i]):
        #             holder = nums[j]
        #             nums[j] = nums[i]
        #             nums[i] = holder

        nums.sort()
        
        for k in range(len(nums) - 1):
            if (nums[k] == nums[k+1]):
                return True

        return False