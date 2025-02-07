class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if s == "":
            return 0
        stack = []
        res = 0
        maxres = 0
        for i in range(len(s)):
            if s[i] == "(":
                if len(stack) == 0:
                    maxres = max(maxres, res)
                    res = 0
                stack.append(s[i])
            elif s[i] == ")":
                if len(stack) != 0:
                    stack.pop()
                    res += 2
                    maxres = max(maxres, res)
                else:
                    maxres = max(maxres, res)
                    res = 0
        return maxres


sol = Solution()
print(sol.longestValidParentheses("((())()"))
print(sol.longestValidParentheses(")))(()()(("))
print(sol.longestValidParentheses(")()())"))
print(sol.longestValidParentheses("(()"))
print(sol.longestValidParentheses("()(()"))
print(sol.longestValidParentheses("()(())"))
