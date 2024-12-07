class Solution(object):
    def __init__(self):
        self.stack = []
    
    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.stack:
            self.stack.pop()


    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        for item in range(len(s)):
            if s[item] == "(":
                self.push(s[item])

            elif s[item] == ")":
                if not self.stack or self.stack[-1] != "(":
                    return False
                self.pop()
            
            if s[item] == "[":
                self.push(s[item])
            elif s[item] == "]":
                if not self.stack or self.stack[-1] != "[":
                    return False
                self.pop()
            
            if s[item] == "{":
                self.push(s[item])
            elif s[item] == "}":
                if not self.stack or self.stack[-1] != "{":
                    return False
                self.pop()
        if len(self.stack) == 0:
            return True

        if len(s) == 1:
            return False
        else: 
            return False
       
          