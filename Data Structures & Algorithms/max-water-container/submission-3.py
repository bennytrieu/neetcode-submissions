class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # output = 0
        # for i in range(len(heights)):
        #     for j in range(i + 1, len(heights)):
        #         height = min(heights[i], heights[j])
        #         width = j - i
        #         output = max(output, height * width)
        # return output
        output = left = 0
        right = 1
        while right < len(heights):
            tall = min(heights[left], heights[right])
            width = right - left
            output = max(output, tall * width)
            right += 1
            if right == len(heights) and left != len(heights) - 1:
                left += 1
                right = left + 1
        return output
            
