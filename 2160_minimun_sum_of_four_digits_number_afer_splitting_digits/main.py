class Solution:
    def minimumSum(self, num: int) -> int:
        
        sorted_num = sorted([int(item) for item in str(num)])
        num2 = 0
        num1 = 0
        
        for i in range(len(sorted_num)):
            if i % 2 == 0:
                num1 = num1 * 10 + sorted_num[i]  
            else:
                num2 = num2 * 10 + sorted_num[i]  
        
        return num1 + num2
    

# num = 4009
num = 2932
s1 = Solution()
print(s1.minimumSum(num))