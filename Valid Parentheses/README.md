## Problem: https://leetcode.com/problems/valid-parentheses/description/
### Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

### Example 1:

Input: s = "()"
Output: true

### Example 2:
Input: s = "()[]{}"
Output: true

### Example 3:
Input: s = "(]"
Output: false

### Example 4:
Input: s = "([])"
Output: true

### Example 5:
Input: s = "([)]"
Output: false

### Constraints:
1 <= s.length <= $$10^4$$
s consists of parentheses only '()[]{}'.

# Solution
## Intuition
For every open paranthesis, check the closest closing paranthesis that is present on its right and check whether all the open parantheses have corresponding closing parantheses and vice versa.


## Approach
The approach is to use a stack data structure and push all the open paranthesis into the stack and for every closing paranthesis, check whether the closing paranthesis is the complement of the stack's top or not. If not push that into stack. Finally, check if the stack is empty or not. If the stack is empty, then the given parantheses is valid else not.

## Complexity
- Time complexity:
$$O(n)$$

- Space complexity:
$$O(n)$$

## Code
```python3 []
class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        op=['(','[','{']
        cl=[')',']','}']
        st=[s[0]]
        for i in range(1,len(s)):
            temp=s[i]
            if st:
                if temp in op:
                    st.append(temp)
                else:
                    ind=cl.index(temp)
                    if st[-1]==op[ind]:
                        st.pop()
                    else:
                        st.append(temp)
            else:
                st.append(temp)
        if st:
            return False
        return True
```
