# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    
    def __init__(self):
        self.head = None
        self.tail = None
    
    def append(self, values):
            for i in values:
                node = ListNode(i)
                if self.head is None:
                    self.head = node
                    self.tail = node
                else:
                    self.tail.next = node
                    self.tail = node
                    
                    
            
    def hasCycle(self):
        visited = set()
        
        temp = self.head
        while temp:
            if temp in visited:
                return True
            visited.add(temp)
            temp  = temp.next
            
        return False
        
        
    
    # def display(self):
    #     temp = self.head
    #     while temp is not None:
    #         print(temp.val)
    #         temp = temp.next
    
    
    
head , pos = [3,2,0,-4], 1
s1 = Solution()

s1.append(head)
# s1.display()
# s1.hasCycle(head)
if pos != -1:
    temp = s1.head
    for i in range(pos):
        temp = temp.next
    
    s1.tail.next = temp
    
print(s1.hasCycle())

        