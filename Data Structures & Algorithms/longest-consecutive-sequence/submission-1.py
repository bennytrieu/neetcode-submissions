class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        print(nums)
        number = 0
        countHolder = 0;
        numHolder = 0;

        if len(nums) == 0:
            return 0

        for i in range(len(nums)):
            if i == 0:
                countHolder+=1
                numHolder = nums[i]
            else:
                if nums[i] == nums[i-1]:
                    continue
                elif nums[i] - 1 == numHolder:
                    countHolder+=1
                    numHolder = nums[i]
                else:
                    countHolder = 1
                    numHolder = nums[i]
            if (countHolder > number):
                number = countHolder
        return number