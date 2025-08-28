class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l=s.split()
        if l:
            return len(l[-1])
        return 0