class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        fizz_buzz_list = []
        for item in range(1, n+1):
            if item % 15 == 0:
                fizz_buzz_list.append("FizzBuzz")
            elif item % 3 == 0:
                fizz_buzz_list.append("Fizz")
            elif item % 5 == 0:
                fizz_buzz_list.append("Buzz")
            
            else:
                fizz_buzz_list.append(str(item))
                
        return fizz_buzz_list
                
    
s1 = Solution()
n = 15
print(s1.fizzBuzz(n))

        
