## Problem: https://leetcode.com/problems/find-smallest-letter-greater-than-target/description/
### 
You are given an array of characters letters that is sorted in non-decreasing order, and a character target. There are at least two different characters in letters.

Return the smallest character in letters that is lexicographically greater than target. If such a character does not exist, return the first character in letters.
### Example 1:
Input: letters = ["c","f","j"], target = "a"
Output: "c"
Explanation: The smallest character that is lexicographically greater than 'a' in letters is 'c'.

### Example 2:
Input: letters = ["c","f","j"], target = "c"
Output: "f"
Explanation: The smallest character that is lexicographically greater than 'c' in letters is 'f'.

### Example 3:
Input: letters = ["x","x","y","y"], target = "z"
Output: "x"
Explanation: There are no characters in letters that is lexicographically greater than 'z' so we return letters[0].

### Constraints:

2 <= letters.length <= $$10^4$$ \\
letters[i] is a lowercase English letter.\\ 
letters is sorted in non-decreasing order.\\
letters contains at least two different characters.\\
target is a lowercase English letter.\\

# Solution

## Approach
The approach is to use the binary search algorithm but the slight modfication, since we want the first greater letter than the target, instead of returing the mid element, we update the position of the letter and update the high value accordingly. 
## Complexity
- Time complexity:
$$O(logn)$$ Where n is the size of the array.

- Space complexity:
$$O(1)$$

## Code
```python3 
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        low = 0
        high = len(letters) - 1
        pos = None
        while low <= high:
            mid = (low + high) // 2
            if letters[mid] > target:
                pos = mid
                high = mid - 1
            else:
                low = mid + 1
        return letters[pos] if pos else letters[0]
```