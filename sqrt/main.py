class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left = 0
        right = x
        
        while left <= right:
            middle = (left + right) // 2
            
            if middle * middle == x:
                return middle
            
            if middle * middle < x:
                left =  middle + 1
            
            elif middle * middle  > x :
                right = middle -1
                
        return right
            
    

s1  = Solution()
print(s1.mySqrt(8))