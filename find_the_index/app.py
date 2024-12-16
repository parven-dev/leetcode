class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        
        if needle in haystack:
            start_index = haystack.find(needle)
            return start_index
        else:
            return -1

s1 = Solution()
# haystack = "hello"
# needle = "ll"
haystack = "leetcode"
needle = "leeto"
# haystack = "sadbutsad"
# needle = "sad"

print(s1.strStr(haystack, needle))