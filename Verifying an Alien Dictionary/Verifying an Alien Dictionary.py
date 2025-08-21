class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        n = len(words)
        for i in range(1, n):
            curr = words[i]
            prev = words[i-1]
            length = min(len(curr), len(prev))
            j = 0
            max_length = max(len(curr), len(prev))
            prev += ' ' * (max_length - length)
            curr += ' ' * (max_length - length)
            while j < max_length and curr[j] == prev[j]:
                j += 1
            if j < max_length and order.find(curr[j]) < order.find(prev[j]):
                return False
        return True