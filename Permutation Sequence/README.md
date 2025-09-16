## Problem: https://leetcode.com/problems/permutation-sequence/description/
### 
The set [1, 2, 3, ..., n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.
 
### Example 1:
Input: n = 3, k = 3
Output: "213"

### Example 2:
Input: n = 4, k = 9
Output: "2314"

### Example 3:
Input: n = 3, k = 1
Output: "123"

### Constraints:
1 <= n <= 9
1 <= k <= n!

# Solution
## Approach
The approach is to first generate all the possible permutations of the given n as a list of integers using backtracking and then when the count is k, return the current permutation.

- Time complexity:
$$O(n!)$$

- Space complexity:
$$O(n)$$

## Code
```python3 []
class Solution:
    def facto(self, n):
        if n == 1:
            return 1
        return n*self.facto(n-1)
    def solve(self, l, n, k, result):
        if n == 1:
            result.append(l[0])
            return
        d = self.facto(n-1)
        x = k//d
        k = k%d
        result.append(l[x])
        l.remove(l[x])
        self.solve(l, n-1, k, result)
    def getPermutation(self, n: int, k: int) -> str:
        l = [str(i) for i in range(1, n+1)]
        result = []
        self.solve(l, n, k-1, result)
        return ''.join(result)
```
