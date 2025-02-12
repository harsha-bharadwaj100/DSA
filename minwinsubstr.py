from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str):
        if not t or not s:
            return ""

        target_counts = Counter(t)
        window_counts = Counter()
        required = len(target_counts)  # Number of unique chars in t
        formed = 0  # Number of characters matched with correct frequency
        min_window_start = 0
        min_window_size = float("inf")

        left = 0
        right = 0

        while right < len(s):
            char = s[right]
            window_counts[char] += 1

            if char in target_counts and window_counts[char] == target_counts[char]:
                formed += 1  # Increment only when the exact count is matched

            while formed == required:  # Shrink only if all required counts are met
                current_window_size = right - left + 1
                if current_window_size < min_window_size:
                    min_window_size = current_window_size
                    min_window_start = left

                left_char = s[left]
                window_counts[left_char] -= 1
                if (
                    left_char in target_counts
                    and window_counts[left_char] < target_counts[left_char]
                ):
                    formed -= 1  # Decrement only when the exact count is no longer met
                left += 1

            right += 1

        if min_window_size == float("inf"):
            return ""
        else:
            return s[min_window_start : min_window_start + min_window_size]


sol = Solution()
print(sol.minWindow("ADOBECODEBANC", "ABC"))
