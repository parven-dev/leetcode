class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        my_index = []
        for i in range(1, len(str1)+1):
            if len(str1) % i == 0 and  len(str2) % i == 0:
                my_index.append(i)
        
        max_index = max(my_index)
        a = len(str1)//max_index
        b = len(str2)//max_index
        common_string  = str1[:max_index]
        string1 = common_string * a
        string2 = common_string * b
        if string1==str1 and string2 == str2:
            return common_string
        else: 
            return ""
        
        # string1 = ""
        # for i in range(len(str1)//2):
        #     string1+=str1[:max_index]
            
        # string2 = ""
        # for i in range(len(str2)//2):
        #     string2+=str2[:max_index]
        
        # print(string1, string2)
            
        # if string2 ==str2 and string1 == str1:
        #     return string1[:max_index]  
        # else:
        #     return ""      
        


s1 = Solution()
str1 = "ABABAB"
str2 = "ABAB"  
# str1 = "ABCABC"
# str2 = "ABC"
str1 = "leet"
str2 = "code"
print(s1.gcdOfStrings(str1, str2))
        