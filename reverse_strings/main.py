class Solution(object):
    def reverseWords(self, s: str):
        """
        :type s: str
        :rtype: str
        """
        # s = s.split(" ")
        # # reverse_string  = s[::-1]
        # for i in (s[::-1]):
        #     print(i, end="")
            
        data = []
        clean_s = " ".join(s.split())
        # print(type(clean_s))
        clean_s = clean_s.split(" ")
        # s = clean_s.split(" ")
        for item in clean_s[::-1]:
            data.append(item)
        
        return " ".join(data)
        # print(reverse_string)
        # reverse_string = reverse_string.split(" ")
        
        # return " ".join(reverse_string[::-1])



s1 = Solution()

s = "a good   example"
print(s1.reverseWords(s))
