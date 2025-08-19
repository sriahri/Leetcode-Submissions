class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        pixelCount = 0
        lines = 0
        for i in range(len(s)):
            letter = s[i]
            pixelCount += widths[ord(letter) - 97]
            if pixelCount > 100:
                pixelCount = widths[ord(letter) - 97]
                lines += 1
        return [lines+1, pixelCount]
