class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        output = 0
        cars = sorted(zip(position, speed), reverse=True)
        stack = []

        for i, s in cars:
            finish = (target - i) / s

            if stack and finish > stack[-1]:
                stack.append(finish)
                output += 1
            elif not stack:
                stack.append(finish)
                output += 1

            # if not stack:
            #     stack.append(finish)
            #     output += 1
            
            # if finish > stack[-1] and finish not in stack:
            #     stack.append(finish)
            #     output += 1

            # if not stack:
            #     stack.append(finish)
            #     output += 1
            # elif finish > stack[-1]:
            #     stack.append(finish)
            #     output += 1
            # elif finish not in stack:
            #     stack.append(finish)
            #     output += 1

            # if stack and finish > stack[-1] and finish not in stack:
            #     stack.append(finish)
            #     output += 1
            # elif not stack:
            #     stack.append(finish)
            #     output += 1
        return output