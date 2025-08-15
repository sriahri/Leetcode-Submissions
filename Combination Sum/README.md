## Problem: https://leetcode.com/problems/combination-sum/
### 
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.
### Example 1:
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.

### Example 2:
Input: n = 1
Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]

### Example 3:
Input: candidates = [2], target = 1
Output: []

### Constraints:
1 <= candidates.length <= 30
2 <= candidates[i] <= 40
All elements of candidates are distinct.
1 <= target <= 40

# Solution

## Approach
The approach is to use the backtracking approach to find the subsequences that sum up to given target. The backtracking approach uses the pick and non pick strategy using the recursion. Since the question says we can use the same element more than once, we will use that concept. If the current element is picked and the target is still less than the target, we will try using the same element again. If the current list of elements does not sum up to the target, we will remove the last added elemnt and try the other elements. If the target is reached, we will add the current list of elements to the resultant list.

## Complexity
- Time complexity:
$$O(2^n)$$

- Space complexity:
$$O(n)$$

## Code
```python3 []
cclass Solution:
    def helper(self, i, result, current, arr, target):
        if i == len(arr):
            if target == 0:
                result.append(current[:])
            return
        if arr[i] <= target:
            current.append(arr[i])
            self.helper(i, result, current, arr, target-arr[i])
            current.pop()
        self.helper(i+1, result, current, arr, target)
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        current = []
        self.helper(0, result, current, candidates, target)
        return result
```
