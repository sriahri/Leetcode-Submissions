## Problem: https://leetcode.com/problems/number-of-equivalent-domino-pairs/description/
### 
Given a list of dominoes, dominoes[i] = [a, b] is equivalent to dominoes[j] = [c, d] if and only if either (a == c and b == d), or (a == d and b == c) - that is, one domino can be rotated to be equal to another domino.

Return the number of pairs (i, j) for which 0 <= i < j < dominoes.length, and dominoes[i] is equivalent to dominoes[j].

### Example 1:
Input: dominoes = [[1,2],[2,1],[3,4],[5,6]]
Output: 1

### Example 2:
Input: dominoes = [[1,2],[1,2],[1,1],[1,2],[2,2]]
Output: 3

### Constraints:
1 <= dominoes.length <= 4 * $$10^4$$ \
dominoes[i].length == 2 \
1 <= dominoes[i][j] <= 9

# Solution
## Approach
The approach is to count all the pairs that are unique and using the count. Find the number of pairs by using $$(n*(n-1))//2$$
## Complexity
- Time complexity:
$$O(n)$$

- Space complexity:
$$O(n)$$

## Code
```python3 []
from collections import Counter
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        for i in range(len(dominoes)):
            dominoes[i] = tuple([min(dominoes[i]), max(dominoes[i])])
        result = 0
        d = Counter(dominoes)
        for k, v in d.items():
            result += (v * (v-1))//2
        return result
```
