class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        para_match = {"(": ")", "[": "]", "{": "}"}
        for i in s:
            if i == "(" or i == "[" or i == "{":
                stack.append(i)
            elif i == ")" or i == "]" or i == "}":
                if not stack:
                    return False
                if i == para_match[stack[-1]]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0  # return true if stack is empty, else false


sol = Solution()
print(sol.isValid("()"))
print(sol.isValid("()[]{}"))
print(sol.isValid("(]"))
print(sol.isValid("([)]"))
print(sol.isValid("{[]}"))
print(sol.isValid("(([[]]))"))
print(sol.isValid("(("))
print(sol.isValid(""))
print(sol.isValid("))"))
print(sol.isValid("}{"))
print(sol.isValid("(}{)"))
