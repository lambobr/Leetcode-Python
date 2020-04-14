"""This function is used to calculate the total number of combinations of 1 and 2 steps in climbing a ladder of n size"""

def climbStairs(n: int) -> int:
        dp = [1]*(n+1)
        print(dp)
        dp[0] = 1
        dp[1] = 2
        for i in range(2,n+1):
            dp[i] = dp[i-1] + dp[i-2]
            print(dp[i])
        return dp[n]
