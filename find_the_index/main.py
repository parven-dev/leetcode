class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        data = []
        for i in range(len(haystack)):
            # print(haystack[i])
            for j in range(i, len(needle)):
                print(needle[j])
                if haystack[j] == needle[i]:
                    # print( haystack[j], needle[i])
                    # index = haystack.index(needle[i])
                    print(needle[i])
                    data.append(needle[i])
        
        print(data)
        
        string = "".join(data)
        
        if string != needle:
            return -1
        else:
            return data.index(string[0])
        
        # if not has_comon:
        #     return -1
        # else:
        #     return data.index(data[0])
        

s1 = Solution()
haystack = "hello"
needle = "ll"
# haystack = "leetcode"
# needle = "leeto"

print(s1.strStr(haystack, needle))