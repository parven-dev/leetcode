class Solution:
    def scoreOfString(self, s: str) -> int:
        
        my_list = []
        
        for i in range(len(s)):
            my_list.append(ord(s[i]))
    
        result = 0
        for j in range(1, len(my_list)):
            k = j - 1
            values =  my_list[k]  - my_list[j] 
            result += (abs(values))
        return result
s = "hello"
s1 = Solution()
print(s1.scoreOfString(s))