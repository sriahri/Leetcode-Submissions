## Problem: https://leetcode.com/problems/lemonade-change/
### 
At a lemonade stand, each lemonade costs $5. Customers are standing in a queue to buy from you and order one at a time (in the order specified by bills). Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill. You must provide the correct change to each customer so that the net transaction is that the customer pays $5.

Note that you do not have any change in hand at first.

Given an integer array bills where bills[i] is the bill the ith customer pays, return true if you can provide every customer with the correct change, or false otherwise.

### Example 1:
Input: bills = [5,5,5,10,20]
Output: true
Explanation: 
From the first 3 customers, we collect three $5 bills in order.
From the fourth customer, we collect a $10 bill and give back a $5.
From the fifth customer, we give a $10 bill and a $5 bill.
Since all customers got correct change, we output true.

### Example 2:
Input: bills = [5,5,10,10,20]
Output: false
Explanation: 
From the first two customers in order, we collect two $5 bills.
For the next two customers in order, we collect a $10 bill and give back a $5 bill.
For the last customer, we can not give the change of $15 back because we only have two $10 bills.
Since not every customer received the correct change, the answer is false.
So [2,2,3,1,4,2] is the shortest subarray, therefore returning 6.

### Constraints:

1 <= bills.length <= $$10^5$$ \
bills[i] is either 5, 10, or 20.

# Solution
## Approach
The approach is to follow the basic conditional statements. Since the bills are only 5, 10, 20. We check if there is a chance of rendering the change or not. For bill 5, no change is required. For bill 10, we need to have atleast 1 bill 5, for bill 20, we need to have 1 bill 10 and 1 bill 5 or 3 bill 5.

## Complexity
- Time complexity:
$$O(n)$$

- Space complexity:
$$O(n)$$

## Code
```python3 []
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        d = {}
        d[5] = 0
        d[10] = 0
        d[20] = 0
        for bill in bills:
            if bill == 5:
                d[5] += 1
            elif bill == 10:
                if d[5] > 0:
                    d[5] -= 1
                    d[10] += 1
                else:
                    return False
            else:
                if d[10] > 0 and d[5] > 0:
                    d[10] -= 1
                    d[5] -= 1
                    d[20] += 1
                elif d[5] >= 3:
                    d[5] -= 3
                    d[20] += 1
                else:
                    return False
        return True
```
