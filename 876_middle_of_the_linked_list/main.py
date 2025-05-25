
from typing import Optional

class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None

class LinkedLIst:
    def __init__(self):
        self.head = None
        self.Tail= None
    
    def insert(self, val):
        new_node = ListNode(val)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            
        else:
            self.tail.next = new_node
            self.tail = new_node
            
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # counter = 0
        temp = head
        slow_pointer = temp
        fast_pointer = temp
        
        while fast_pointer and fast_pointer.next:
            # print(slow_pointer.val, end="->")

            slow_pointer = slow_pointer.next
            # counter+=1
            # print(fast_pointer.val, end="->")
            fast_pointer = fast_pointer.next.next
        # print(slow_pointer.val)
                        # print(fast_pointer.val, end="->")
        # slow_pointer = slow_pointer.next
        # print(slow_pointer.val)              
        dummy = ListNode(0)
        current = dummy
        temp2 = slow_pointer
        while temp2:
            current.next = temp2
            current = temp2
            temp2 = temp2.next
            
        current.next = None
        return dummy.next
            

    def display(self, head):
        temp = head
        
        while temp is not None:
            print(temp.val)
            temp = temp.next



ll = LinkedLIst() 

my_list = [1,2,3,4,5]
my_list = [1,2,3,4,5,6]
for num in my_list:
    ll.insert(num)
    
# ll.display()
result = ll.middleNode(ll.head)
print(ll.display(result))