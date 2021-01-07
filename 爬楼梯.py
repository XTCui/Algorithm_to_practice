from functools import lru_cache

class Solution:
    @lru_cache(maxsize=None)
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1
        if n ==2: return 2
        return self.climbStairs(n-1)+self.climbStairs(n-2)



# class Solution:
#     def climbStairs(self, n: int) -> int:
#         dp={}
#         dp[1]=1
#         dp[2]=2
#         for i in range(3,n+1):
#             dp[i] = dp[i-1] + dp[i-2]
#         return dp[n]