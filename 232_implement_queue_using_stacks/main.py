class MyQueue:

    def __init__(self):
        self.my_queue = []

    def push(self, x: int) -> None:
        self.my_queue.append(x)

    def pop(self) -> int:
        if not self.empty():
            return self.my_queue.pop(0)  
        raise IndexError("pop from an empty queue") 

    def peek(self) -> int:
        if not self.empty():
            return self.my_queue[0]  
        raise IndexError("peek from an empty queue")  

    def empty(self) -> bool:
        return len(self.my_queue) == 0  
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()