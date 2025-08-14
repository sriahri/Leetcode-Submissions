class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            return haystack.index(needle)
        return -1

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        window = len(needle)
        i = 0
        while i <= n - window:
            if haystack[i:i+window] == needle:
                return i
            i += 1
        return -1