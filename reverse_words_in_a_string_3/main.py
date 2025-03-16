class Solution:
    def reverseWords(self, s: str) -> str:
        string = []
        my_string = s.split()
        
        for item in my_string:
            string.append(item[::-1])
            
        return " ".join(string)
    
    
s1 = Solution()
s = "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"
print(s1.reverseWords(s))