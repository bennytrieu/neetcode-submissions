class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temp = temperatures
        n = len(temp)
        output = [0] * n
        stack = []

        for i, t in enumerate(temp):
            while stack and stack[-1][0] < t:
                stack_t, stack_i = stack.pop()
                output[stack_i] = i - stack_i
            stack.append([t, i])
        return output