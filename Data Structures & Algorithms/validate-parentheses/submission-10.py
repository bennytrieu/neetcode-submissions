class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        characters = {"(" : ")", "{" : "}", "[": "]"}

        for c in s:
            if stack and c == characters[stack[-1]]:
                stack.pop()
            elif c == "(" or c == "{" or c == "[":
                stack.append(c)
            else:
                return False

        if stack:
            return False
        else:
            return True