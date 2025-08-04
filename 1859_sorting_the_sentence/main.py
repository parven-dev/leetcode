class Solution:
    def sortSentence(self, s: str) -> str:
        split_string = s.split( )
        my_dict = {}
        for item in split_string:
            only_num = item[-1]
            my_dict[only_num] = item[:-1]
            
        result = []
        
        for key in sorted(my_dict):
            result.append(my_dict[key])
            
        return  .join(result)
        
    

s1 = Solution()
s = is2 sentence4 This1 a3
print(s1.sortSentence(s)) 
