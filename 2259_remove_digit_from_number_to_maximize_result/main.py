class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        max_value = []
        
        for i in range(len(number)):
            if number[i] == digit:
                data = number[:i] + number[i+1:]
                max_value.append(data)
                
                
        return max(max_value)

s1 = Solution()
# number = "123"
# digit = "3"  

number = "1231"
digit = "1"
print(s1.removeDigit(number, digit))
