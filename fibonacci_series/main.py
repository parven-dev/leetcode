class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if n in (0,1,2):
            return 1
        else:
            return self.fib(n-1) + self.fib(n-2)
            
    
    

s1 = Solution()
n = 5
print(s1.fib(n))