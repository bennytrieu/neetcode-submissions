class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = 1
        while left < right:
            if (numbers[left] + numbers[right] == target):
                return [left + 1, right + 1]
            right+=1
            if right == len(numbers):
                left+=1
                right = left + 1
                
