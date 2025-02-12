class Solution:
    def addToArrayForm(self, num: list[int], k: int) -> list[int]:
        
        num = "".join(map(str, num))
        data = int(num) + k
        
        result = []
        for item in str(data):
            result.append(int(item))
            
            
        return result
            
        
     
    


s1 = Solution()
num = [1,2,0,0]
k = 34

print(s1.addToArrayForm(num, k))