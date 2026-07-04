class Solution:
    def maxArea(self, heights: List[int]) -> int:
        output = 0
        for i in range(len(heights)):
            for j in range(i + 1, len(heights)):
                height = min(heights[i], heights[j])
                width = j - i
                output = max(output, height * width)
        return output