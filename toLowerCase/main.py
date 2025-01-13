class Solution(object):
    def toLowerCase(self, s):
        """
        :type s: str
        :rtype: str
        """

        string = ""
        for item in s:
            if item.isupper():
                string+=item.lower()
            else:
                string+=item
        return string