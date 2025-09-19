def numSquareSum(n): 
    squareSum = 0; 
    while(n): 
        squareSum += (n % 10) * (n % 10); 
        n = int(n / 10); 
    return squareSum;
class Solution:
    def isHappy(self, n: int) -> bool:
        slow = n; 
        fast = n; 
        while(True): 

            # move slow number 
            # by one iteration 
            slow = numSquareSum(slow); 

            # move fast number 
            # by two iteration 
            fast = numSquareSum(numSquareSum(fast)); 
            if(slow != fast): 
                continue; 
            else: 
                break; 

        # if both number meet at 1,  
        # then return true 
        return (slow == 1);