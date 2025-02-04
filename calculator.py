class Solution:
    def calculate(self, s: str) -> int:
        """Constraints:

        1 <= s.length <= 3 * 105
        s consists of digits, '+', '-', '(', ')', and ' '.
        s represents a valid expression.
        '+' is not used as a unary operation (i.e., "+1" and "+(2 + 3)" is invalid).
        '-' could be used as a unary operation (i.e., "-1" and "-(2 + 3)" is valid).
        There will be no two consecutive operators in the input.
        Every number and running calculation will fit in a signed 32-bit integer.
        No usage of eval is allowed.
        """
        stack = []
        num = 0
        sign = 1
        result = 0
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c == "+":
                result += sign * num
                num = 0
                sign = 1
            elif c == "-":
                result += sign * num
                num = 0
                sign = -1
            elif c == "(":
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
            elif c == ")":
                result += sign * num
                num = 0
                result *= stack.pop()
                result += stack.pop()
        return result + sign * num


sol = Solution()
print(sol.calculate("1 + 1"))  # 2
print(sol.calculate(" 2-1 + 2 "))  # 3
print(sol.calculate("(1+(4+5+2)-3)+(6+8)-(1+2)"))  # 23
print(sol.calculate("1"))  # 1
print(sol.calculate(" - 1 + 1"))  # 2
