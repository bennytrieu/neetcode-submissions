class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsMap = {}
        arr = []

        for i in range(len(nums)):
            numsMap[nums[i]] = 1 + numsMap.get(nums[i], 0)
        
        sortedNums = sorted(numsMap, key=numsMap.get, reverse=True)
        print(sortedNums)

        for j in range(k):
            arr.append(sortedNums[j])

        return arr