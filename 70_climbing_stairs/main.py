class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        
        def climbStairs_helper(n: int) -> int:

            if n == 1:
                return 1
            if n == 2 :
                return 2
            
            if n in memo:
                return memo[n]
        
            result = climbStairs_helper(n-1) + climbStairs_helper(n-2)
        
            memo[n] = result
            print(memo)
            return result
        
        return climbStairs_helper(n)
 


s1 = Solution()
n = 5
print(s1.climbStairs(n))