class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            ssum = 0
            while n != 0:
                rem = n % 10
                ssum += rem**2
                n = int(n / 10)
            n = ssum
        return n == 1


s = Solution()
print(s.isHappy(2))
