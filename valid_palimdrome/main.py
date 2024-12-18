class Solution(object):
    def isPalindrome(self, s:str):
        """
        :type s: str
        :rtype: bool
        """
        
        s = "".join(char.lower() for char in s if char.isalnum() )
        data = []
        for i in range(len(s)):
            pointer = s[i]
            reverse_pointer = s[len(s)-1-i]
            if pointer == reverse_pointer:
                data.append(pointer)
                
        if len(data) == len(s):
            return True
        else:
            return False

s1 = Solution()
s = "A man, a plan, a cnal: Panama"
print(s1.isPalindrome(s))