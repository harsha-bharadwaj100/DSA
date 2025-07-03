from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs):
        anagram_map = defaultdict(list)

        for word in strs:
            sorted_word = "".join(sorted(word))  # Sort each word
            anagram_map[sorted_word].append(word)  # Group by sorted word

        return list(anagram_map.values())


# test
s = Solution()
print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(s.groupAnagrams([""]))
print(s.groupAnagrams(["a"]))
