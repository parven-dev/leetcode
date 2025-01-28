# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
class Solution(object):
    
    def __init__(self):
        self.head = None
        self.tail = None
    
    def append(self, value):
        for item in value:
            node = ListNode(item)
            
            if self.head is None:
                self.head = node
                self.tail = node
            else:
                self.tail.next = node
                self.tail = node
                
                
    def display(self):
        temp = self.head
        while temp is not None:
            # print(type(temp))
            print(temp.val)
            temp = temp.next
    
    def deleteDuplicates(self):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        node = self.head
        while node and node.next:
            
            if node.val == node.next.val:
                node.next = node.next.next
            else:
                node = node.next
            
        return self.head
                
            
    
    


# head = [1,1,2,3,3]
head = [1,1,2]
s1 = Solution()
s1.append(head)
print(s1.display())
s1.deleteDuplicates()
print("after ")
print(s1.display())