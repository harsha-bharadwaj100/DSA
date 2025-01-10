class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j = 0, 1
        length = len(s)
        result = 0
        while j <= length:
            sety = set(s[i:j])
            if len(s[i:j]) == len(sety):
                result += 1
                j += 1
            else:
                i += 1
                j += 1
        return result


sol = Solution()
print(sol.lengthOfLongestSubstring(""))
