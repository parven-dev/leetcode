class Solution:
    def firstPalindrome(self, words: list[str]) -> str:
        
        for word in words:
            if self.check_palindrome(word):
                return word
            return 
        
    def check_palindrome(self, value):
        if len(value) == 0:
            return True
        start = 0
        end = len(value)-1

        while start < end:
            if value[start] != value[end]:
                return False
         
            start+=1
            end-=1
           
            
        return True
            
    
    
# words = [abc,car,ada,racecar,cool]
words = [def,ghi]
s1 = Solution()
print(s1.firstPalindrome(words))

arr = [1,2,3,4,5,6]

# for i in range(len(arr)):
#     print(arr[i], arr[len(arr)-i-1] ) 
