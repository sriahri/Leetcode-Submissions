from collections import Counter
from math import gcd
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        d = Counter(deck)
        count = list(d.values())
        divisor = count[0]
        for i in count[1:]:
            divisor = gcd(divisor, i)
        if divisor <= 1:
            return False
        return True