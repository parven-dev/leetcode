class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        maximum_value = []  
        s = s.split(" ")
        for item in s:
            item_len = len(item)
            if item_len:
                maximum_value.append(item_len)
        
        
        max_value = maximum_value[-1]
        print(max_value)

s1 = Solution()
# s = "Today is a nice day"
s = "   fly me   to   the moon  "
print(s1.lengthOfLastWord(s))