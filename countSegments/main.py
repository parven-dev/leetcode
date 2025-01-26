class Solution:
    def countSegments(self, s: str) -> int:
        
        s = s.split()
        return len(s)
        
        # s = "".join(s)
        
        print(len(s))
          
        
        # if s == "":
        #     return 0
        # else:
        #     return len(ss)     
    
s = "Hello, my name is John"
# s = "    "
s1 = Solution()
print(s1.countSegments(s))