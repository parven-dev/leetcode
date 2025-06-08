class Solution:
    def convertDateToBinary(self, date: str) -> str:
        list_of_date = date.split("-")
        binary_date = []
        for item in list_of_date:
            to_binary = bin(int(item))
            binary_date.append(to_binary[2:])
            
        return "-".join(binary_date)
    
    
s1 = Solution()
print(s1.convertDateToBinary( date = "2080-02-29"))