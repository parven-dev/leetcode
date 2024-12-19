class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s = sorted(s)
        t = sorted(t)
        
        if s == t:
            return True
        else:
            return False
      
                



s1 = Solution()
s = "aacc"
t = "ccac"
print(s1.isAnagram(s, t))
