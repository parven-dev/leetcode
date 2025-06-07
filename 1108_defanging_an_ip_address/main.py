class Solution:
    def defangIPaddr(self, address: str) -> str:
        my_list = []
        
        for ids in  address:
            if ids == ".":
                my_list.append("[.]")
            else:
                my_list.append(ids)

        return  "".join(my_list)
    
    
s1 = Solution()
address = "1.1.1.1"
print(s1.defangIPaddr(address))