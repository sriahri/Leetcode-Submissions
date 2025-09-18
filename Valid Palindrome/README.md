## Problem: https://leetcode.com/problems/valid-palindrome/description/
### 

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

### Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

### Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

### Example 3:
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

### Constraints:
1 <= s.length <= 2 * $$10^5$$
s consists only of printable ASCII characters.

# Solution
## Approach
The approach is to remove all the numeric characters and convert all the uppercase to lowercase and check if the resultant string is a palindrome or not.

## Complexity
- Time complexity:
$$O(n)$$

- Space complexity:
$$O(n)$$

## Code
```python3 []
class Solution:
    def isPalindrome(self, s: str) -> bool:
        x=''
        for i in s:
            if i.isalnum():
                x+=i.lower()
        if x==x[::-1]:
            return True
        return False
```
