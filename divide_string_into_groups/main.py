class Solution:
    def divideString(self, s: str, k: int, fill: str) -> list[str]:
        
        s = [i for i in s ]
        my_list = []
        index1 = 0
        index2 = k
        for _ in range(len(s)):
            data = s[index1:index2]
        #    print(index1, index2)
            if len(data) == k:
                my_list.append(data)
            
            if len(data) > 0 and len(data) < k:
                check = k - len(data) 
                for _ in range(check):
                    data.append(fill)
                my_list.append(data)
            
            index1+=k
            index2+=k
           
       
       
        final_result  =  ["".join(item)for item in my_list]
        return final_result
           


s1 = Solution()
  
s = "abcdefghi"
k = 3
fill = "x"
print(s1.divideString(s, k, fill))