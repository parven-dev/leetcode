class Solution():
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ss = 0
        tt = 0
       
        if not s:
            return True
        while ss < len(s) and tt < len(t):
            if s[ss] == t[tt]:
                ss+=1
            tt+=1

        return ss == len(s)

s1 = Solution()
print(s1.isSubsequence(s="abc", t="ahbgdc"))