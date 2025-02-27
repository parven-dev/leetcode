class Solution(object):
    def maxDistance(self, colors):
        """
        :type colors: List[int]
        :rtype: int
        """
        
        max_value = 0
        n = len(colors)
        
        left = 0
        
        while colors[left] == colors[-1]:
            left +=1 
            
        right = n -1 
        while colors[right] == colors[0]:
            right-=1
            
        
        return max(n-1-left, right)
  
  
        
colors = [1,1,1,6,1,1,1]
s1 = Solution()
print(s1.maxDistance(colors))
