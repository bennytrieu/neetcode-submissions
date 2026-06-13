class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if (len(nums) == 2):
            return [0,1]
        
        hashmap = {}
        for i, num in enumerate(nums):
            hashmap[num] = i
        print(hashmap)

        for j in range(len(nums)):
            holder = target - nums[j]
            print(holder)
            if holder in hashmap and hashmap[holder] != j:
                return [j, hashmap[holder]]
            holder = target