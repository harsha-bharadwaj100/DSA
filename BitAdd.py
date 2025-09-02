class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = "0"
        sum = "0"
        res = ""
        alen, blen = len(a), len(b)
        diff = alen - blen
        if diff > 0:
            b = "0" * diff + b
        elif diff < 0:
            a = "0" * -diff + a
        ptr = max(alen, blen) - 1
        while ptr >= 0:
            if carry != "1":
                sum = (
                    "1"
                    if a[ptr] == "1"
                    and b[ptr] == "0"
                    or a[ptr] == "0"
                    and b[ptr] == "1"
                    else "0"
                )
                carry = "1" if a[ptr] == b[ptr] == "1" else "0"
            else:
                sum = (
                    "0"
                    if a[ptr] == "1"
                    and b[ptr] == "0"
                    or a[ptr] == "0"
                    and b[ptr] == "1"
                    else "1"
                )
                carry = "0" if a[ptr] == b[ptr] == "0" else "1"
            res += sum
            ptr -= 1
        return res[::-1]


sol = Solution()
print(sol.addBinary("11", "100"))
print(sol.addBinary("0001001010000001", "010100110101"))
print(sol.addBinary("0001011110110101", "010100110101"))
