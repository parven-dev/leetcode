class Solution:
    def finalValueAfterOperations(self, operations: list[str]) -> int:
        X = 0
        
        for operation in operations:
            if operation.startswith("++") or operation.endswith("++"):
                X+=1
            else:
                x-=1
                
        return X
    
    
    
    
    
operations = ["++X","++X","X++"]
s1 = Solution()
print(s1.finalValueAfterOperations(operations))
