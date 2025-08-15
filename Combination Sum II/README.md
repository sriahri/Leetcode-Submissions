## Problem: https://leetcode.com/problems/combination-sum-ii/description/
### 
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

### Example 1:
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]

### Example 2:
Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]

### Constraints:
1 <= candidates.length <= 30
2 <= candidates[i] <= 50
1 <= target <= 30

# Solution

## Approach
The approach is to use the backtracking approach to find the subsequences that sum up to given target. The backtracking approach uses the pick and non pick strategy using the recursion. Since the question says we cannot use the same element more than once, we will use that concept. If the current element is picked and the target is still less than the target, we will check for the next elements. If the current list of elements does not sum up to the target, we will remove the last added element and try the other elements. If the target is reached, we will add the current list of elements to the resultant list.

## Complexity
- Time complexity:
$$O(2^n)$$

- Space complexity:
$$O(n)$$

## Code
```python3 []
class Solution:
    def helper(self, ind, target, arr, current, result):
        if target == 0:
            result.append(current[:])
            return
        for i in range(ind, len(arr)):
            if i > ind and arr[i] == arr[i-1]:
                continue
            if arr[i] > target:
                break
            current.append(arr[i])
            self.helper(i+1, target-arr[i], arr[:], current, result)
            current.pop()
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        self.helper(0, target, candidates, [], result)
        return result
```
