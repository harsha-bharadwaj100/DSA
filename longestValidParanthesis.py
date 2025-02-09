class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if s == "":
            return 0
        left, right, maxres = 0, 0, 0
        for i in range(len(s)):
            if s[i] == "(":
                left += 1
            else:
                right += 1
            if left == right:
                maxres = max(maxres, 2 * left)
            elif right > left:
                left, right = 0, 0

        left, right = 0, 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "(":
                left += 1
            else:
                right += 1
            if left == right:
                maxres = max(maxres, 2 * left)
            elif left > right:
                left, right = 0, 0
        return maxres


sol = Solution()
print(sol.longestValidParentheses("((())()"))
print(sol.longestValidParentheses(")))(()()(("))
print(sol.longestValidParentheses(")()())"))
print(sol.longestValidParentheses("(()"))
print(sol.longestValidParentheses("()(()"))
print(sol.longestValidParentheses("()(())"))
