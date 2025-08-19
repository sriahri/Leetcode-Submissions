class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower()
        for char in "!?',;.":
            paragraph = paragraph.replace(char, ' ')
        d = {}
        result = None
        maxi = 0
        for word in paragraph.split():
            word = word.strip()
            if word not in banned:
                if word in d:
                    d[word] += 1
                else:
                    d[word] = 1
        for word in d.keys():
            if d[word] > maxi:
                maxi = d[word]
                result = word
        return result
