## Problem: https://leetcode.com/problems/contains-duplicate-ii/description/
### 
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

### Example 1:
Input: nums = [1,2,3,1], k = 3
Output: true

### Example 2:
Input: nums = [1,0,1,1], k = 1
Output: true

### Example 3:
Input: nums = [1,2,3,1,2,3], k = 2
Output: false

### Constraints:
1 <= nums.length <= $$10^5$$
-$$10^9$$ <= nums[i] <= $$10^9$$
0 <= k <= $$10^5$$

# Solution
## Approach
The approach is to use a set and queue. Use a set to check if the element is present in the set or not. Use a queue to insert and pop elements so that the length is used to check with k and determine if the repeated element index is less than k or not.

## Complexity
- Time complexity:
$$O(n)$$

- Space complexity:
$$O(n)$$

## Code
```python3 []
from collections import Counter
class Solution:
    def containsNearbyDuplicate(self, l: List[int], k: int) -> bool:
        # n=len(l)
        # d=Counter(l)
        # for i in d.keys():
        #     if d[i]>1:
        #         j=l.index(i)
        #         y=l[::-1].index(i)
        #         y=n-y
        #         for x in range(j,y):
        #             if l[x] in l[x+1:k+x+1]:
        #                 return True
        # return False
        q=[]
        s=set()
        for i in l:
            if i in s:
                return True
            q.append(i)
            s.add(i)
            if len(q)>k:
                j=q.pop(0)
                s.remove(j)
        return False
```