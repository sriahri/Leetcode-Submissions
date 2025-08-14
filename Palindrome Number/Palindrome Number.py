class Solution:
    def isPalindrome(self, x: int) -> bool:
        s=str(x)
        if s[0]=='-':
            return False
        a=s[::-1]
        if s==a:
            return True
        return False
    
class Solution:
    def isPalindrome(self, x: int) -> bool:
        res = 0
        copy = x
        if x < 0:
            return False
        while x != 0:
            res = res * 10 + x%10
            x = x//10
        if res == copy:
            return True
        return False