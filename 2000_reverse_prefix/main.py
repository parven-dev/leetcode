class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        my_stack = []
        my_stack1 = ""

        
        index = 0      
        for i in range(len(word)):
            if word[i] == ch:
                index = i
                break
        
        for char in word[:index+1]:
            my_stack.append(char)
        
        while my_stack:
            my_stack1+=my_stack.pop()
            
        return my_stack1+word[index+1:]
            
#output dcbaefd

s1 = Solution()
word = "abcdefd"
ch = "d"
print(s1.reversePrefix(word, ch))