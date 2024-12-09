class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        list_items = list(str(x))
        
        palindrome_list = []
        
        for i in range(len(list_items)):
            reverse = list_items[len(list_items) -1 -i]
            if reverse  == list_items[i]:
                palindrome_list.append(reverse)   
                     
        if list_items == palindrome_list:
            return True
        else:
            return False
       

s1 = Solution()
print(s1.isPalindrome(x=121))